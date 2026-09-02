# ai-researcher

AI 관련 뉴스·논문·업계 동향을 자동으로 모아 **하루 두 번(09:00 / 19:00 KST)** 한국어 브리핑으로 만들어 주는 개인용 파이프라인입니다.

[Thysrael/Horizon](https://github.com/Thysrael/Horizon)(MIT)을 포크해 한국어 출력, arXiv 수집, 단계별 모델 라우팅, 하루 2회 스케줄, 맥/폰 알림을 더했습니다.

## 동작 방식

```
GitHub Actions (00:00 · 10:00 UTC)
  └─ 수집  arXiv(아침만) · Hacker News · Reddit · RSS 22종 · GitHub 릴리스 · Google News
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
| GitHub Pages | 웹에서 열람 (저장소 Settings → Pages → `gh-pages` 브랜치) |
| ntfy 푸시 | 폰 알림. 상위 5건 제목이 본문에 들어감 |
| 맥 알림센터 | launchd 폴러가 새 브리핑 도착 시 배너 표시 |

## 최초 설정

### 1. GitHub Secrets 등록

저장소 → Settings → Secrets and variables → Actions → New repository secret.

| 이름 | 필수 | 용도 |
|---|---|---|
| `ANTHROPIC_API_KEY` | **필수** | 채점·요약. [console.anthropic.com](https://console.anthropic.com/settings/keys)에서 발급 |
| `NTFY_TOPIC` | 선택 | 폰 푸시. 추측 불가능한 문자열을 직접 정하세요 (예: `ai-brief-8f3k2p9x`) |
| `APIFY_TOKEN` | 선택 | X(트위터) 수집을 켤 때만 |

> **주의**: 이 저장소는 public입니다. 키를 파일에 적어 커밋하지 마세요. `data/config.json`, `.env`, `data/x_cookies_*.json`은 `.gitignore`로 막혀 있습니다.

### 2. ntfy 폰 푸시 (선택)

1. 폰에 [ntfy 앱](https://ntfy.sh/) 설치 (iOS / Android, 무료·가입 불필요)
2. 앱에서 `NTFY_TOPIC`에 넣은 것과 **같은 토픽**을 구독

토픽 이름을 아는 사람은 누구나 그 알림을 볼 수 있으니 길고 무작위한 문자열을 쓰세요.

### 3. Actions 활성화

포크된 저장소는 Actions가 기본 비활성입니다. 저장소 → Actions 탭 → 워크플로 활성화.

첫 실행은 Actions → **AI Briefing** → *Run workflow*로 수동 확인하는 것을 권합니다.

### 4. 맥 알림 설정

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

### 논문은 아침 브리핑에만 들어갑니다

arXiv는 하루 한 번, 18:00 UTC 직전 타임스탬프로 묶어서 공개합니다. 13시간 수집 창 기준으로 아침 실행(00:00 UTC)은 이 배치를 포함하지만 저녁 실행(10:00 UTC)은 창이 배치보다 뒤에서 시작해 논문을 하나도 못 잡습니다. 논문이 원래 하루 한 번 나오므로, 저녁 실행에서는 arXiv를 꺼서 헛돌지 않게 했습니다.

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
