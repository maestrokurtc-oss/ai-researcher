# ai-researcher

## [🌅 AI 리서처 브리핑 바로 보기](https://maestrokurtc-oss.github.io/ai-researcher/)

AI 관련 뉴스·논문·업계 동향을 자동으로 모아 **하루 두 번(09:17 / 19:17 KST)** 한국어 브리핑으로 만들어 주는 개인용 파이프라인입니다.

[Thysrael/Horizon](https://github.com/Thysrael/Horizon)(MIT)을 포크해 한국어 출력, arXiv 수집, 단계별 모델 라우팅, 하루 2회 스케줄, 맥/폰 알림을 더했습니다.

## 동작 방식

```
GitHub Actions (00:17 · 10:17 UTC)
  └─ 수집  arXiv(아침만) · GeekNews(핵심) · Hacker News · Reddit · RSS 22종 · GitHub 릴리스 · Google News
  └─ 채점  Haiku 4.5 로 중요도 0~10 점수화 + 프로필 분류
  └─ 선별  프로필별 임계값 통과분만 남기고 주제 중복 제거
  └─ 요약  Sonnet 5 로 한국어 요약 작성
  └─ 산출  briefings/YYYY/MM/YYYY-MM-DD-{morning,evening}.md 커밋
           + GitHub Pages 배포 + ntfy 폰 푸시
        ↓
맥 launchd (30분마다)  git pull → 새 브리핑이면 알림센터 배너
```

## 브리핑 읽는 곳

| 경로 | 설명 |
|---|---|
| `briefings/2026/09/2026-09-02-morning.md` | 저장소에 커밋되는 원본. 맥에서 `git pull` 후 바로 열림 |
| [GitHub Pages](https://maestrokurtc-oss.github.io/ai-researcher/) | 웹에서 바로 열람 |
| ntfy 푸시 | 폰 알림. 상위 5건 제목이 본문에 들어감 |
| 맥 알림센터 | launchd 폴러가 새 브리핑 도착 시 배너 표시 |

## 최초 설정

### 1. GitHub Secrets 등록

저장소 → Settings → Secrets and variables → Actions → New repository secret.

| 이름 | 필수 | 용도 |
|---|---|---|
| `ANTHROPIC_API_KEY` | **필수** | 채점·요약. [console.anthropic.com](https://console.anthropic.com/settings/keys)에서 발급 |
| `GMAIL_APP_PASSWORD` | 크레딧 메일 사용 시 | `maestrokurtc@gmail.com`에서 발급한 Google 앱 비밀번호. 부족 예상·실행 실패 메일 전송에만 사용 |
| `NTFY_TOPIC` | 선택 | 폰 푸시. 추측 불가능한 문자열을 직접 정하세요 (예: `ai-brief-8f3k2p9x`) |
| `APIFY_TOKEN` | 선택 | X(트위터) 수집을 켤 때만 |

> **주의**: 이 저장소는 public입니다. 키나 앱 비밀번호를 파일, 이슈, 채팅에 적지 말고 GitHub Secret 입력 화면에만 넣으세요. `data/config.json`, `.env`, `data/x_cookies_*.json`은 `.gitignore`로 막혀 있습니다.

### 2. Anthropic 크레딧 사전 경고 설정

일반 Anthropic API 키로는 선불 크레딧 잔액을 조회할 수 없습니다. 따라서 Anthropic Console에 현재 표시된 **실제 가용 잔액**을 기준점으로 저장하고, 이후 이 저장소가 기록한 모델별 토큰 비용을 빼서 남은 실행 횟수를 보수적으로 추정합니다. 기본값은 최소 $2 또는 최근 평균 4회분 중 더 큰 금액이 남았을 때 경고하는 것입니다.

저장소 → Settings → Secrets and variables → Actions → **Variables**에서 다음 값을 등록합니다.

| 이름 | 필수 | 예시·설명 |
|---|---|---|
| `ANTHROPIC_CREDIT_BASELINE_USD` | **필수** | Console에서 방금 확인한 가용 잔액(USD), 예: `20.00` |
| `ANTHROPIC_CREDIT_BASELINE_AT` | **필수** | 잔액을 확인한 UTC 시각, 예: `2026-09-12T12:00:00Z` |
| `ANTHROPIC_CREDIT_WARN_BELOW_USD` | 선택 | 절대 경고선, 기본 `2.00` |
| `ANTHROPIC_CREDIT_RESERVE_RUNS` | 선택 | 확보할 실행 회차 수, 기본 `4` |
| `CREDIT_ALERT_EMAIL_TO` | 선택 | 수신 주소, 기본 `maestrokurtc@gmail.com` |
| `GMAIL_SMTP_USERNAME` | 선택 | 발신 Gmail, 기본 `maestrokurtc@gmail.com` |

Google 계정에서 2단계 인증을 켠 뒤 앱 비밀번호를 만들어 `GMAIL_APP_PASSWORD` GitHub Secret으로 등록합니다. 설정 후 Actions → **Diagnostics** → `credit-email`을 실행하면 실제 테스트 메일을 보낼 수 있습니다.

충전할 때마다 Console의 새 가용 잔액과 그 확인 시각으로 두 기준 변수를 함께 갱신하세요. 이 추정치는 이 프로젝트에서 기록한 호출만 반영하므로, 같은 Anthropic 계정의 다른 프로젝트가 크레딧을 쓰는 경우 Console의 자동 충전도 함께 켜는 편이 안전합니다. 크레딧과 무관하게 모델 사전 점검 또는 본 실행이 실패해도 같은 Gmail 주소로 즉시 알립니다.

### 3. ntfy 폰 푸시 (선택)

1. 폰에 [ntfy 앱](https://ntfy.sh/) 설치 (iOS / Android, 무료·가입 불필요)
2. 앱에서 `NTFY_TOPIC`에 넣은 것과 **같은 토픽**을 구독

토픽 이름을 아는 사람은 누구나 그 알림을 볼 수 있으니 길고 무작위한 문자열을 쓰세요.

### 4. Actions 활성화

포크된 저장소는 Actions가 기본 비활성입니다. 저장소 → Actions 탭 → 워크플로 활성화.

첫 실행은 Actions → **AI Briefing** → *Run workflow*로 수동 확인하는 것을 권합니다.

### 5. 맥 알림 설정

```bash
./local/install.sh
```

30분마다 `git pull` 후 새 브리핑이 있으면 알림을 띄웁니다. 해제는 `./local/install.sh --uninstall`.

알림을 클릭해 파일을 바로 열고 싶다면 `brew install terminal-notifier`를 먼저 설치하세요. 없으면 클릭 동작 없는 기본 알림으로 동작합니다.

## 소스 점검 (API 키 불필요)

수집 단계만 돌려 어떤 소스가 몇 건을 주는지 확인합니다. 모델을 호출하지 않으므로 비용이 들지 않습니다.

```bash
cp data/config.github.json data/config.json
uv run python scripts/check-sources.py            # 설정된 창으로 전체 수집
uv run python scripts/check-sources.py --hours 24 # 창을 넓혀서
uv run python scripts/check-sources.py --feeds    # RSS URL 응답만 빠르게
```

## 수집 소스 바꾸기

전부 [`data/config.github.json`](data/config.github.json) 한 곳에서 조정합니다. 코드 수정은 필요 없습니다.

- **RSS 추가**: `sources.rss`에 `{ "name": ..., "url": ..., "category": ..., "profile": ... }` 추가
- **RSS별 선정 문턱**: `sources.rss[].selection_threshold` — 해당 피드만 프로필 문턱을 덮어씁니다. GeekNews는 핵심 소스로 6.0을 적용합니다
- **arXiv 카테고리**: `sources.arxiv.categories`
- **중요도 문턱 조정**: `processing.profile_settings.<프로필>.threshold` — 브리핑이 너무 길면 올리고, 너무 짧으면 내립니다
- **브리핑 분량**: `digest.max_items`

### 프로필

항목의 성격에 따라 다른 채점 기준과 요약 형식을 적용합니다.

| 프로필 | 대상 | 문턱 |
|---|---|---|
| `ai-paper` | arXiv 논문 (이 포크에서 추가) | 7.5 |
| `tech-news` | 뉴스·커뮤니티·랩 발표·릴리스 | 7.0 |
| `tech-blog` | 뉴스레터·장문 분석 | 6.0 |

## 비용

| 단계 | 모델 | 단가 (1M 토큰) |
|---|---|---|
| 중요도 채점 · 주제 중복 제거 | `claude-haiku-4-5` | 입력 $1 / 출력 $5 |
| 한국어 요약 작성 | `claude-sonnet-5` | 입력 $2 / 출력 $10 |

수집량 대부분(회당 100~150건)은 저렴한 채점 단계에서 걸러지고, 비싼 요약 단계에는 문턱을 넘은 20여 건만 올라갑니다. 모델은 `data/config.github.json`의 `ai.model`(요약)과 `ai.stage_models`(채점·중복제거)에서 바꿀 수 있습니다.

## X(트위터)에 대해

`sources.twitter.enabled`가 `false`로 꺼져 있습니다. Horizon의 X 수집은 두 가지 모드뿐인데,

- `playwright` — 본인의 X 로그인 쿠키 파일이 필요합니다. public 저장소 시크릿에 계정 자격증명을 넣는 셈이고 X 이용약관 위반이라 설정하지 않았습니다.
- `apify` — [Apify](https://apify.com/) 유료 토큰이 필요합니다.

Apify를 쓰시려면 `APIFY_TOKEN` 시크릿을 등록하고 `enabled`를 `true`로 바꾸면 됩니다. 그동안 X의 AI 담론은 Import AI, Interconnects, Latent Space, Simon Willison, Ahead of AI 등 뉴스레터 피드가 상당 부분 대신 덮습니다.

### 정시 배달은 보장되지 않습니다

GitHub 의 예약 실행은 공유 러너에서 최선노력으로 처리됩니다. 부하가 몰리면 몇 시간씩 밀리고, 가장 붐비는 시각에는 실행이 통째로 누락됩니다. 실제로 자정 정각 UTC 로 잡았던 아침 실행이 한 번 누락됐고, 저녁 실행은 4시간 지연된 적이 있습니다.

그래서 크론을 정시에서 비켜 `:17` 로 두고, 슬롯마다 2시간 뒤 재시도를 하나씩 더 겁니다. 해당 슬롯의 브리핑 파일이 이미 있으면 재시도는 아무 것도 하지 않고 끝나므로 중복 비용이 없습니다. 슬롯은 실행 시각이 아니라 **트리거한 크론 식**으로 판정하므로, 아침 실행이 아무리 밀려도 저녁으로 오인되어 arXiv 가 꺼지는 일은 없습니다.

두 번 다 누락되면 그 회차는 건너뜁니다. Actions 탭에서 *Run workflow* 로 `slot` 을 지정해 직접 돌릴 수 있습니다.

### 논문은 아침 브리핑에만 들어갑니다

arXiv는 하루 한 번, 18:00 UTC 직전 타임스탬프로 묶어서 공개합니다. 13시간 수집 창 기준으로 아침 실행(00:17 UTC)은 이 배치를 포함하지만 저녁 실행(10:17 UTC)은 창이 배치보다 뒤에서 시작해 논문을 하나도 못 잡습니다. 논문이 원래 하루 한 번 나오므로, 저녁 실행에서는 arXiv를 꺼서 헛돌지 않게 했습니다.

## 알려진 한계

- **회차 간 중복**: 수집 창이 13시간이라 12시간 간격 실행과 1시간 겹칩니다. 실행 지연으로 소식을 놓치는 것보다 낫다고 판단한 트레이드오프로, 드물게 같은 항목이 두 브리핑에 나올 수 있습니다.
- **The Batch**: RSS를 제공하지 않아 제외했습니다.
- **Anthropic 공식 블로그**: 공식 RSS가 없어 커뮤니티 미러 두 곳을 씁니다. 미러가 죽으면 조용히 빠집니다.

## 개발

```bash
uv sync --extra dev
uv run pytest -q
```

```bash
cp data/config.github.json data/config.json
ANTHROPIC_API_KEY=... uv run python -m src.main --hours 13 --log-level INFO
```

## 이 포크가 upstream과 다른 점

| 변경 | 파일 |
|---|---|
| arXiv 스크레이퍼 (카테고리별 질의 + 429 재시도) | `src/scrapers/arxiv.py` |
| 단계별 모델 라우팅 (`ai.stage_models`) | `src/ai/client.py` |
| 한국어 출력 | `src/ai/summarizer.py`, `src/ai/prompting/enrichment.py` |
| 논문 전용 프로필 | `profiles/ai-paper/` |
| 하루 2회 실행 + 브리핑 보존 + ntfy | `.github/workflows/briefing.yml` |
| 맥 알림 폴러 | `local/` |

upstream 문서는 [UPSTREAM_README.md](UPSTREAM_README.md)에 남겨두었습니다. 최신 변경을 가져오려면:

```bash
git fetch upstream && git merge upstream/main
```

## 라이선스

MIT. [Thysrael/Horizon](https://github.com/Thysrael/Horizon)의 저작권 표시는 [LICENSE](LICENSE)에 그대로 유지됩니다.
