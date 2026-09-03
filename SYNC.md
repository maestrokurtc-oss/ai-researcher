# 검토대 동기화 절차

브리핑은 GitHub Actions 에서 돌고, 마킹은 claude.ai 의 Artifact 페이지에서
한다. 둘은 서로에게 직접 쓸 수 없다 — Actions 는 Artifact 데이터베이스에
접근할 수 없고, Artifact 페이지는 CSP 때문에 외부 주소를 fetch 할 수 없다.
그래서 Claude 세션이 양쪽을 오가며 잇는다. 이 문서가 그 절차다.

검토대: https://claude.ai/code/artifact/7000b6ea-aa4d-45c2-9aff-a9f71d2185b4

## 1. 저장소 → 검토대 (새 탈락 후보 올리기)

```bash
git pull --rebase origin main
uv run python scripts/prepare-db-docs.py
```

아직 올리지 않은 회차만 `.sync/db-docs/<회차>.json` 으로 준비되고, 회차 키가
`.sync/synced-runs.json` 에 기록된다. 준비된 파일마다 Artifact 툴로:

- `action: write_db`, `db_op: set`
- `collection: runs`, `doc_id: <파일 이름에서 .json 을 뺀 것>`
- `file_path: .sync/db-docs/<그 파일>`

회차당 문서 하나에 항목 배열을 담는다. 항목마다 문서를 만들면 문서 5,000개
상한에 몇 달 만에 닿는다.

## 2. 검토대 → 저장소 (마킹을 채점에 반영)

Artifact 툴로 마킹을 내려받는다.

- `action: read_db`, `db_op: list`, `collection: marks`
- `out_dir: .sync/marks`

```bash
uv run python scripts/apply-marks.py .sync/marks/
git add data/interests.json && git commit -m "관심사 프로필 갱신" && git push origin main
```

`data/interests.json` 은 다음 브리핑의 채점 프롬프트에 실린다. 마킹이 하나도
없으면 스크립트는 기존 프로필을 덮어쓰지 않고 종료한다 — 읽기 실패와
"아직 표시한 것이 없음" 을 구분할 수 없기 때문이다.

## 3. 오래된 회차 정리

문서 상한이 5,000개다. 회차당 하나씩 쌓이므로 하루 2개, 연 730개다. 한동안은
여유가 있지만, 아주 오래된 회차는 `write_db` 의 `delete` 로 지운다. 저장소의
`near-misses/` 아카이브는 그대로 남으므로 기록이 사라지지는 않는다.
