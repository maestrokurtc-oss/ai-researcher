# AI 리서처 피드백 저장소

GitHub Pages에 게시된 AI 리서처 브리핑의 `좋아요`·`별로예요` 선택을
Cloudflare D1에 append-only 이벤트로 저장하는 Sites/vinext 서비스입니다.

## 동작

- `POST /api/v1/feedback`: 공개 보고서의 콘텐츠 반응 저장
- `OPTIONS /api/v1/feedback`: GitHub Pages origin용 CORS preflight
- 보고서별 정적 manifest에 있는 콘텐츠만 허용
- `event_id` unique key로 네트워크 재시도 멱등성 보장
- 브라우저 UUID는 서버 HMAC 후 저장하고 원본 값은 보관하지 않음
- 원 IP는 저장하지 않고 HMAC한 rate-limit key는 2시간 뒤 만료 처리
- 전역·네트워크·브라우저별 시간당 제한으로 기본적인 자동화 오염 완화

환경 변수는 Sites에만 저장합니다.

- `VOTER_HMAC_SECRET` (secret, 32자 이상)
- `ALLOWED_ORIGIN`
- `REPORT_DATA_ORIGIN`

## 데이터 해석

`feedback_events`는 이력 보존을 위해 수정하지 않습니다. 반응 변경과 취소도
각각 새 이벤트이며 `clear`가 취소를 뜻합니다. 현재 선호를 집계할 때는 같은
`(report_id, content_key, voter_hash)` 그룹에서 가장 큰
`sequence` 하나만 남긴 뒤 `clear`를 제외해야 합니다.

```sql
WITH latest AS (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY report_id, content_key, voter_hash
    ORDER BY sequence DESC
  ) AS row_number
  FROM feedback_events
)
SELECT report_id, content_key, title, surface, ai_score,
       SUM(reaction = 'like') AS likes,
       SUM(reaction = 'dislike') AS dislikes
FROM latest
WHERE row_number = 1 AND reaction != 'clear'
GROUP BY report_id, content_key, title, surface, ai_score;
```

익명 공개 반응은 조작 가능성을 완전히 제거할 수 없는 참고 신호입니다. 기존
운영자 평가와 섞어 자동 반영하지 말고, 기간·출처·점수·표본 수와 함께 검토해
선별 개선에 사용합니다.

## 개발

저장소 루트에서 서비스 디렉터리로 이동한 뒤 잠금 파일 기준으로 설치합니다.

```bash
cd services/feedback-api
npm ci
npm run db:generate
npm run build
npm run lint
npm test
```
