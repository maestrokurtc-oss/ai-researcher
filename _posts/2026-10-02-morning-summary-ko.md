---
layout: default
title: "AI 브리핑 · 2026-10-02 아침"
report_id: "2026-10-02-morning"
date: 2026-10-02
lang: ko
---

> 수집한 153건 중 14건을 골랐습니다.

---

**업계 동향**
1. [SvelteKit 3 출시, 타입 안전성과 개발 경험 개선에 집중](#item-tech-news-1) ⭐️ 7.0/10
2. [모델이 직접 컨텍스트를 편집하는 Context Language Models\(CLM\) 제안](#item-tech-news-2) ⭐️ 7.0/10
3. [Tencent, AI 인프라·에이전트 보안 점검용 오픈소스 레드팀 플랫폼 공개](#item-tech-news-3) ⭐️ 7.0/10
4. [ESP32 칩의 숨겨진 IQ 샘플링 기능으로 SDR 구현 가능성 발견](#item-tech-news-4) ⭐️ 7.0/10
5. [Cloudflare K2, R2 기반 서버리스 이벤트 스트리밍 공개 베타 출시](#item-tech-news-5) ⭐️ 7.0/10
6. [터미널 코딩 에이전트 Pi, 1.0 버전 정식 출시](#item-tech-news-6) ⭐️ 6.0/10
7. [Pi Durable, 장시간 실행 AI 에이전트를 위한 내구성 실행 환경](#item-tech-news-7) ⭐️ 6.0/10
8. [Git 3.0의 SHA-256 기본값 전환, 비용 문제인가 보안 조치인가](#item-tech-news-8) ⭐️ 6.0/10
9. [arXiv, 제출 급증 대응해 월간 및 동시 제출 건수 제한 도입](#item-tech-news-9) ⭐️ 6.0/10
10. [Debian, Linux 커널 다중 취약점 보안 패치 DSA-6528-1 발행](#item-tech-news-10) ⭐️ 6.0/10
11. [OpenAI, 안전 연구원 3명과 결별…WSJ 보도](#item-tech-news-11) ⭐️ 6.0/10
12. [Google, 새 Gemini AI 모델 출시하며 안전 우려로 접근 제한](#item-tech-news-12) ⭐️ 6.0/10
13. [Apollo, 일본 150억 달러 규모 AI 인프라 프로젝트 지원](#item-tech-news-13) ⭐️ 6.0/10

**심층 분석 · 뉴스레터**
1. [RLM과 에이전트 하네스: Alex Zhang가 말하는 학계의 위험한 베팅](#item-tech-blog-1) ⭐️ 6.0/10

---

## 업계 동향

<a id="item-tech-news-1"></a>
### [SvelteKit 3 출시, 타입 안전성과 개발 경험 개선에 집중](https://svelte.dev/blog/sveltekit-3-is-here) ⭐️ 7.0/10

Svelte 공식 애플리케이션 프레임워크인 SvelteKit의 3.0 버전이 출시되었다. 기존 아키텍처는 그대로 유지하면서 완성도와 타입 안전성을 높이고 불필요한 상용구 코드를 줄이는 데 초점을 맞췄다. sv migrate 도구가 가능한 코드 변경을 자동으로 처리하고, 수동 작업이 필요한 부분은 TODO 목록으로 생성해주지만 메이저 버전업에 따른 호환성 파괴 변경 사항은 별도로 확인해야 한다. 주요 변경으로는 설정 파일이 vite.config.ts로 이동한 점, $lib 별칭이 표준 서브패스 임포트 방식인 \#lib로 대체된 점, 환경 변수 처리 개선, 서비스 워커 상용구 축소, 전반적인 오류 처리 향상 등이 있다. 다만 Remote functions 기능은 아직 완성되지 않았으며 Async Svelte 지원이 필요한 최우선 개발 과제로 남아 있다.

hackernews · sampsn · 10월 1일 20:14 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49926536)

**「배경」** SvelteKit은 컴파일 타임에 반응형 UI 코드를 최적화하는 Svelte 프레임워크 위에 구축된 공식 풀스택 애플리케이션 프레임워크로, 라우팅·서버 사이드 렌더링·빌드 설정 등을 제공한다. React나 Next.js 같은 가상 DOM 기반 프레임워크와 달리 Svelte는 컴파일 단계에서 반응성을 처리해 런타임 오버헤드가 적고 문법이 순수 HTML/JS에 가깝다는 평가를 받아왔다.

**「영향」** 기존 SvelteKit 사용자는 vite.config.ts 설정 이전, $lib에서 \#lib로의 별칭 변경 등 호환성 파괴 변경을 sv migrate로 상당 부분 자동 전환할 수 있지만, 나머지 수동 작업과 호환성 검토는 직접 수행해야 한다.

**「커뮤니티 반응」** 댓글 작성자들은 React나 Next.js 경험과 비교해 Svelte/SvelteKit의 개발 경험과 HTML에 가까운 문법을 긍정적으로 평가했으며, Wails와 결합해 20MB 미만의 경량 바이너리로 데스크톱·모바일 앱을 만든 사례처럼 다목적 활용성도 언급되었다. 또한 최근 고급 LLM들이 과거와 달리 Svelte 4/5 코드를 안정적으로 생성할 수 있게 되었다는 의견이 있었으나, 바이브 코딩 경험이 React 대비 실제로 다른지에 대해서는 명확한 답이 제시되지 않았다.

**태그**: `#frontend-framework`, `#sveltekit`, `#web-development`, `#developer-experience`

---

<a id="item-tech-news-2"></a>
### [모델이 직접 컨텍스트를 편집하는 Context Language Models\(CLM\) 제안](https://news.hada.io/topic?id=34653) ⭐️ 7.0/10

Context Language Models\(CLM\)는 외부 하네스가 고정된 규칙으로 압축·요약을 수행하던 기존 방식 대신, 모델이 현재 컨텍스트를 파일처럼 직접 읽고 편집하며 필요한 정보를 스스로 유지·갱신하는 접근이다. 추가 학습 없이 기존 모델에 적용했을 때 BrowseComp-Plus에서 정확도가 가장 강력한 비교 방법\(Codex 방식 요약\) 대비 11.4% 높았고 접두부 재사용 FLOPs는 21.5% 적었으며, TerminalBench 2.1과 TBLite 등 장시간 코딩·조사 과제에서도 유사한 성능·효율 개선이 관찰됐다. 자연어 지시나 스킬 문서 최적화만으로도 관리 정책을 유도할 수 있어 ContextBench에서 미사용 평가 데이터 기준 정확도가 최대 35.9%p 상승했고, 강화학습\(단계별 GRPO와 성공 조건부 효율 이점\)을 적용한 Qwen3.5-9B는 BrowseComp-Plus 정확도가 28.8%에서 42.5%로 올랐다. 컨텍스트 중간 편집 후 남은 토큰의 캐시를 재사용하는 Suffix Cache Reuse\(SCR\) 기법은 동일 정확도\(60.2%\)를 유지하면서 서버 측 FLOPs를 표준 SGLang 대비 35% 추가로 절감했다.

rss · GeekNews · 10월 2일 04:35

**「배경」** 기존 언어 모델 에이전트는 컨텍스트 길이가 늘어나면 외부 하네스가 정해둔 규칙\(일정 길이 도달 시 압축, 턴마다 요약 등\)에 따라 과거 기록을 요약하거나 삭제하는데, 이는 정보 손실·환각·불필요한 재계산 같은 한계를 안고 있었다. Recursive Language Models나 ACM, Sculptor 같은 선행 연구들은 모델의 자율성을 일부 넓혔지만 사람이 정의한 동작 범위 안에서만 작동했으며, CLM은 이런 제한을 없애고 컨텍스트 전체의 관리 권한을 모델에 넘긴다는 점에서 차별화된다.

**「영향」** 장시간 실행되는 에이전트형 코딩·조사 작업을 설계하는 개발자들에게는 하네스 수준의 고정된 압축 로직 대신 모델이 스스로 컨텍스트를 관리하게 함으로써 정확도와 연산 비용을 동시에 개선할 여지가 생긴다. 다만 편집 가능한 컨텍스트는 프롬프트 인젝션이나 모델이 스스로 삽입한 지시가 여러 턴에 걸쳐 지속되는 새로운 보안 위험을 수반하므로, 실제 배포 전에는 별도의 방어 체계와 공격 표면 분석이 필요하다.

**태그**: `#large-language-models`, `#context-management`, `#model-optimization`, `#inference-efficiency`, `#ai-systems`

---

<a id="item-tech-news-3"></a>
### [Tencent, AI 인프라·에이전트 보안 점검용 오픈소스 레드팀 플랫폼 공개](https://news.hada.io/topic?id=34645) ⭐️ 7.0/10

Tencent가 공개한 AI-Infra-Guard는 AI 인프라와 에이전트의 보안을 점검하는 오픈소스 레드팀 플랫폼으로, v4.6.0 기준 146개 AI 구성요소와 2,000개 이상의 CVE 규칙을 지원한다. Ollama, ComfyUI, vLLM, n8n 등 실행 중인 서비스 주소를 입력하면 구성요소와 버전을 식별해 알려진 취약점을 탐지하고, MCP Server·Agent Skill 분석을 통해 도구 오염·자격 증명 유출·명령어 주입·악성 코드·권한 상승 위험을 검사한다. Agent Scan은 Dify, Coze 등의 워크플로를 여러 에이전트로 자동 평가해 도구 오용과 데이터 유출 가능성을 탐색하며, OpenClaw 전용 ClawScan, 탈옥 공격 저항성 평가, LLM API 블랙박스 감사\(모델 정체 및 중계 과정 바꿔치기·백도어 징후 검사\) 기능도 포함한다. 웹 UI와 API, 독립 CLI\(skill-scan, mcp-scan, agent-scan\)로 기존 보안 점검 절차에 통합 가능하며, 검사 규칙과 탈옥 평가 데이터셋은 파일 기반 플러그인으로 확장할 수 있고 Docker로 Linux, macOS, Windows에서 실행되며 Apache-2.0 라이선스로 배포된다. 다만 자체 인증 기능이 없어 공개 네트워크에 직접 노출하지 않고 내부 환경에서만 사용해야 한다는 제약이 있다.

rss · GeekNews · 10월 2일 00:30

**「배경」** 레드팀\(red team\)은 공격자 관점에서 시스템의 취약점을 사전에 찾아내는 보안 점검 방식으로, 최근 LLM과 AI 에이전트가 서버·도구·외부 API와 연동되며 프롬프트 인젝션, 탈옥, 자격 증명 유출 같은 새로운 공격 표면이 생겨났다. MCP\(Model Context Protocol\)는 LLM이 외부 도구나 데이터 소스와 통신하도록 표준화한 연결 규격으로, Tencent는 Black Hat Europe 2025 Arsenal 발표를 통해 MCP 생태계를 노리는 공급망 공격 가능성을 지적하며 AI-Infra-Guard의 필요성을 설명한 바 있다.

**「영향」** AI 인프라와 에이전트 기반 서비스를 운영하는 조직이 취약점 스캐닝부터 에이전트 행동 감사, LLM 탈옥 저항성 평가까지 단일 도구로 통합 점검할 수 있게 되어 보안 점검 비용과 복잡도가 줄어들 것으로 보인다. 다만 자체 인증 기능 부재로 내부 전용 배치가 전제되어야 하며, 공개 노출 시 오히려 공격 표면이 될 수 있다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://github.com/Tencent/AI-Infra-Guard">GitHub - Tencent / AI - Infra - Guard : A full-stack AI Red Teaming ...</a></li>

</ul>
</details>

**태그**: `#ai-security`, `#open-source`, `#vulnerability-scanning`, `#agent-testing`, `#red-teaming`

---

<a id="item-tech-news-4"></a>
### [ESP32 칩의 숨겨진 IQ 샘플링 기능으로 SDR 구현 가능성 발견](https://news.hada.io/topic?id=34635) ⭐️ 7.0/10

ESPARGOS 팀은 여러 ESP32 마이크로컨트롤러에서 고정된 WiFi/Bluetooth 기능을 우회해 원시 IQ 기저대역 샘플을 수집할 수 있는 미문서화 기능을 발견했다. 이 기능으로 칩에 따라 최대 80 MS/s 샘플링 속도와 약 13~54 MHz 아날로그 대역폭을 지원하며, 대부분 모델은 2.2~2.7 GHz\(ESP32-C5는 4.8~6.0 GHz도 지원\)를 다루지만 출력 대역폭 부족으로 PC에는 데이터 스냅샷만 전송 가능해 스펙트럼 분석기 용도로 제한된다. 반면 ESP32-S31은 Gigabit Ethernet을 통해 최대 16 MS/s 연속 스트리밍이 가능하며, GNU Radio·gqrx용 SoapySDR 드라이버도 곧 제공될 예정이다. ESPARGOS는 위상 정합 IQ 수집을 활용해 WiFi/Bluetooth뿐 아니라 2.4 GHz 대역의 임의 신호에 대한 방향 탐지도 가능해졌다고 밝혔으며, 비슷한 시기에 Reddit 사용자 /u/h0m3us3r가 FPGA를 USB3 프런트엔드로 쓴 ESP32-S3 연속 스트리밍 SDR을, C5VRX 프로젝트가 ESP32-C5 기반 5.8 GHz FPV 영상 수신기를 각각 독립적으로 공개해 유사 기능이 동시다발적으로 발견되고 있음을 보여준다.

rss · GeekNews · 10월 1일 21:32

**「ESP32와 ESPARGOS 프로젝트 배경」** ESP32는 Espressif Systems가 만든 저가형 Wi-Fi/Bluetooth 내장 마이크로컨트롤러로, IoT 기기에 널리 쓰이지만 무선 기능은 고정된 전용 모뎀 회로를 통해서만 동작하도록 설계되어 있다. ESPARGOS는 2025년 공개된 프로젝트로, 여러 ESP32 보드와 패치 안테나를 배열해 Wi-Fi 신호의 도래 방향을 실시간으로 탐지하는 위상 배열 시스템이며, 이번 발견은 그 연장선에서 ESP32 칩 내부의 숨겨진 IQ 샘플링 경로를 찾아낸 것이다. 소프트웨어 정의 라디오\(SDR\)는 하드웨어 대신 소프트웨어로 신호 복조·분석을 수행하는 방식으로, 이번 발견은 저가 범용 칩을 SDR 장비로 전용할 수 있는 가능성을 연다.

**「영향」** 저렴하고 널리 쓰이는 ESP32 칩이 별도 하드웨어 없이도 스펙트럼 분석, 방향 탐지, FPV 수신 등 SDR 응용에 활용될 수 있게 되어 RF 취미·연구 커뮤니티와 오픈소스 하드웨어 프로젝트에 새로운 실험 기반을 제공한다. 다만 클록 품질, 연속 스트리밍 대역폭, 원거리 수신 신뢰성 등 현재의 기술적 한계로 인해 범용 SDR 수준의 완성도에는 아직 도달하지 못했다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://espargos.net/espsdr/">ESPARGOS - ESP-SDR: Raw IQ Capture with Espressif&#x27;s ESP32 Chips</a></li>
<li><a href="https://github.com/ESPARGOS/esp-sdr">GitHub - ESPARGOS/esp-sdr: ESP-SDR uses the undocumented raw I/Q ...</a></li>

</ul>
</details>

**태그**: `#hardware`, `#embedded-systems`, `#sdr`, `#esp32`, `#reverse-engineering`

---

<a id="item-tech-news-5"></a>
### [Cloudflare K2, R2 기반 서버리스 이벤트 스트리밍 공개 베타 출시](https://news.hada.io/topic?id=34629) ⭐️ 7.0/10

Cloudflare가 서버리스 이벤트 스트리밍 서비스 K2의 공개 베타를 출시했다. K2는 R2 객체 스토리지를 기반으로 이벤트를 순서형 로그에 저장해 생산자와 소비자를 분리하며, 여러 독립적인 소비자가 각자의 속도로 전체 이벤트를 읽거나 하나의 구독에서 작업을 나눠 병렬 처리할 수 있다. 개별 작업 재시도에 초점을 둔 Queues와 달리 대량 데이터 전달과 장기 보관에 적합하며, 배치 단위로 처리하되 메시지 단위 재시도는 지원하지 않고 초기 버전의 쓰기 요청 지연은 p99 기준 약 1초다. Workers 유료 구독 계정에서 베타 기간 중 추가 과금 없이 사용 가능하며 초기 한도는 저장 공간 10GB, 스트림당 쓰기 처리량 30MB/s이고, 향후 쓰기 병렬성 확대, 키 기반 순서 보장, 푸시 기반 Worker 소비자, Express 등급, Apache Kafka 클라이언트 호환 지원이 계획되어 있다.

rss · GeekNews · 10월 1일 19:53

**「배경」** 전통적인 RPC 구조에서는 생산자가 소비자의 처리 능력을 초과하거나 소비자가 중단되면 이벤트가 유실될 수 있어, Kafka 같은 분산 이벤트 로그가 이를 해결하는 수단으로 쓰여왔다. K2는 원래 Basin Pipelines의 수집 계층을 위한 내구성 있는 엣지 버퍼로 개발되었으며, 335개 이상 도시에 분산된 Cloudflare 엣지 환경에서는 Kafka 같은 전통적 분산 시스템을 그대로 운영하기 어렵기 때문에 R2의 강한 일관성과 원자적 연산을 활용해 복제와 합의를 스토리지 계층에 위임하는 방식을 택했다.

**「영향」** Cloudflare Workers 생태계 개발자는 별도 Kafka 클러스터를 운영하지 않고도 다중 소비자 이벤트 분배 아키텍처를 구축할 수 있게 되어, Queues\(개별 작업 재시도\)와 Pipelines\(객체 스토리지·Iceberg 적재\) 사이의 빈틈이었던 대규모 이벤트 스트리밍 요구를 충족할 수 있다. 다만 현재 한도\(저장 10GB, 30MB/s\)와 초 단위 생산 지연, 메시지 단위 재시도 미지원은 고처리량·저지연이 필요한 프로덕션 워크로드 적용에는 제약으로 작용할 수 있다.

**태그**: `#serverless`, `#event-streaming`, `#cloudflare`, `#distributed-systems`, `#infrastructure`

---

<a id="item-tech-news-6"></a>
### [터미널 코딩 에이전트 Pi, 1.0 버전 정식 출시](https://earendil.com/posts/pi-1-0/) ⭐️ 6.0/10

여러 AI 모델을 지원하는 터미널 코딩 에이전트 Pi가 1.0 버전을 출시했다. 매주 수십만 명이 사용해온 이 프로젝트는 수개월간의 사용자 피드백을 반영해 안정성을 개선했으며, Codemode 기능을 통해 JavaScript로 여러 도구 호출을 조합할 수 있다. 1.0 버전은 MCP\(Model Context Protocol\) 도구, Jev 같은 의사결정 모델, 이미지 모델을 함께 사용하도록 지원하며, 여러 모델을 하나처럼 다루는 가상 모델 확장 기능도 포함한다. Pi는 최소한의 시스템 프롬프트 오버헤드를 특징으로 하며, 이는 로컬 모델 환경에서의 실행 성능에 직접적인 영향을 준다.

hackernews · sergiotapia · 10월 1일 19:33 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49926069)

**「배경」** Pi는 Earendil이 개발한 터미널 기반 코딩 에이전트로, 통합 LLM API와 에이전트 루프, TUI, CLI를 제공하는 오픈소스 AI 에이전트 툴킷이다. MCP\(Model Context Protocol\)는 에이전트가 외부 도구와 데이터 소스에 표준화된 방식으로 연결하도록 해주는 프로토콜로, Pi는 이를 통해 다양한 모델과 도구를 조합해 사용할 수 있다.

**「영향」** 로컬 모델 환경에서 작업하는 개발자들은 Pi의 최소화된 시스템 프롬프트 덕분에 저사양 하드웨어에서도 실용적인 프리필 속도를 얻게 되며, Claude·Codex 등 여러 에이전트 간 skill·MCP 설정을 따로 관리하던 번거로움을 줄일 수 있다. 다만 히스토리 되돌림 버그나 Anthropic 캐시 워밍 기능이 별도 패키지로 분리되지 않은 점 등은 여전히 실무 적용 시 해결해야 할 과제로 남아 있다.

**「커뮤니티 반응」** 사용자들은 Pi가 비대한 시스템 프롬프트 없이도 로컬 모델에서 안정적으로 동작하는 몇 안 되는 에이전트라는 점과 미니멀리즘·확장성을 장점으로 꼽으며, 코딩 전용을 넘어 OS 범용 에이전트로 점진적으로 확장해 사용하는 사례를 공유했다. 다만 추론 중 히스토리가 처음으로 되돌아가는 버그에 대한 불만과, Anthropic 모델용 캐시 워밍 기능이 왜 별도 패키지로 분리되지 않고 '미니멀'을 표방하는 코어에 번들되었는지에 대한 비판도 제기되었다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://earendil.com/posts/pi-1-0/">Pi 1.0 | Earendil</a></li>
<li><a href="https://github.com/earendil-works/pi">GitHub - earendil-works/pi: AI agent toolkit: unified LLM API, agent ...</a></li>

</ul>
</details>

**태그**: `#agent-framework`, `#open-source`, `#local-models`, `#extensibility`, `#developer-tools`

---

<a id="item-tech-news-7"></a>
### [Pi Durable, 장시간 실행 AI 에이전트를 위한 내구성 실행 환경](https://earendil.com/posts/pi-durable/) ⭐️ 6.0/10

Pi Durable는 장시간 실행되는 AI 에이전트를 안정적으로 운영하기 위한 내구성 있는 실행 환경을 제공하는 도구로, 전체 소스 코드는 테스트를 제외하고 약 15,000줄 규모다. 설계상 특징으로 대화 분기\(branching conversation tree\)는 지원하지 않고, 조상 정보\(ancestry\)를 포함한 대화 포크\(fork\)만 지원하는 선택을 했는데, 이 결정이 내구성 보장에 꼭 필요한지에 대해 커뮤니티에서 의문이 제기되었다. 또한 동일한 소스 코드가 GPT 기준 약 150,000토큰, Claude 기준 약 250,000토큰으로 계산되어 토큰 집계 방식의 차이가 크다는 점도 언급되었다. 이 도구는 LangChain Deep Agents, Vercel Eve, OpenAI Agents API, Anthropic Managed Agents 등 주요 업체들이 비슷한 목적으로 제품을 개발 중인 활발한 영역에 속한다.

hackernews · paulsmith · 10월 1일 19:24 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49925969)

**「배경」** Pi Durable은 Earendil이 Pi 1.0과 함께 공개한 실험적 패키지로, 대화·모델 턴·도구 호출 등 에이전트의 모든 상태를 저장소에 커밋한 뒤에만 처리를 진행해, 프로세스가 중간에 죽어도 중단된 지점부터 재개할 수 있게 설계된 '내구성 있는\(durable\) 에이전트 하네스'다. 이는 사람이 지켜보지 않아도 장시간·무인으로 안전하게 돌아갈 수 있는 에이전트 인프라에 대한 업계 전반의 수요에서 비롯된 것으로, LangChain의 Deep Agents, Vercel의 eve, OpenAI Agents API, Anthropic의 Managed Agents 등 주요 플랫폼들도 비슷한 durable execution 개념의 프레임워크를 경쟁적으로 선보이고 있다.

**「영향」** 장시간 무인 실행이 필요한 AI 에이전트 시스템을 구축하는 개발자들에게 내구성 실행 아키텍처의 설계 트레이드오프\(포크 대 분기, 샌드박싱 부재 등\)를 가늠할 수 있는 또 하나의 구체적 구현 사례를 제공한다. 다만 아직 샌드박싱을 1급 기능으로 지원하지 않는다는 한계가 지적되어, 신뢰할 수 없는 컨텍스트를 다루는 실무 적용에는 제약이 따를 수 있다.

**「커뮤니티 반응」** 댓글에서는 LangChain, Vercel, OpenAI, Anthropic 등도 유사한 내구성 에이전트 하네스를 만들고 있다는 점이 언급되며 이 분야가 코딩 에이전트만큼 화제성은 적지만 활발한 혁신 영역이라는 평가가 있었고, 대화 분기 미지원 결정의 필요성과 소스 코드의 토큰 수 산정 방식 차이에 대한 기술적 의문이 제기되었다. 일부 사용자는 샌드박싱과 신뢰되지 않은 컨텍스트 격리가 여전히 1급 기능으로 다뤄지지 않는다는 점에 아쉬움을 표했고, 이런 무한 실행 에이전트의 실제 활용 사례가 무엇인지 묻는 질문도 있었다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://earendil.com/posts/pi-durable/">Pi Durable | Earendil</a></li>
<li><a href="https://github.com/earendil-works/pi/tree/main/packages/durable">pi/packages/durable at main · earendil-works/pi · GitHub</a></li>
<li><a href="https://docs.langchain.com/oss/python/deepagents/customization">Customize Deep Agents - Docs by LangChain</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/5338/vercel-eve-open-source-framework-ai-agents">Vercel eve : the Open-Source Next.js for AI Agents | Pasquale Pillitteri</a></li>

</ul>
</details>

**태그**: `#ai-agents`, `#agent-infrastructure`, `#durable-execution`, `#software-engineering`, `#open-source`

---

<a id="item-tech-news-8"></a>
### [Git 3.0의 SHA-256 기본값 전환, 비용 문제인가 보안 조치인가](https://blog.gitbutler.com/git-3-sha-256) ⭐️ 6.0/10

이 블로그 글은 Git 3.0에서 SHA-256을 기본 해시 알고리즘으로 채택하려는 계획이 마이그레이션 비용에 비해 실질적인 보안 이점이 크지 않다고 주장한다. 저자는 GitHub 등 주요 포지\(forge\)들이 SHA-256 저장소를 제대로 지원하지 않는 상황과 서브모듈 호환성 문제 등을 근거로 이번 전환이 생태계 전반에 큰 부담을 줄 것이라고 지적한다. 그러나 커뮤니티에서는 2017년 공개된 SHAttered 공격이 SHA-1에 대한 실제 충돌\(collision\) 공격의 실용적 증명 사례였다는 점, 그리고 저장소 간 코드 스머글링 문제에는 충돌 공격만으로도 충분히 위협이 될 수 있다는 점을 들어 저자가 SHA-1의 위험성을 과소평가했다고 반박한다. 또한 GitHub의 SHA-256 지원 현황에 대한 저자의 묘사가 실제와 다르며, 저장소에 처음 푸시된 데이터를 기준으로 해시 포맷을 결정하는 방식은 불가능한 문제가 아니라는 지적도 나왔다.

hackernews · chmaynard · 10월 1일 16:57 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49924179)

**「배경」** Git은 오랫동안 커밋과 객체를 식별하는 데 SHA-1 해시를 사용해 왔으나, 2017년 구글과 CWI Amsterdam이 발표한 SHAttered 공격으로 SHA-1에서 실제 충돌을 생성할 수 있음이 증명되면서 보안 우려가 제기되었다. 이에 Git은 2020년 2.29 버전부터 --object-format=sha256 옵션으로 SHA-256 해시를 선택적으로 지원해 왔지만, SHA-1과 SHA-256 저장소 간에는 상호 운용성이 없고 GitHub 등 주요 호스팅 플랫폼은 아직 SHA-256 저장소를 지원하지 않는 상태다. Git 3.0에서는 이 SHA-256을 신규 저장소의 기본 해시 알고리즘으로 전환할 계획인데, 이는 서브모듈 호환성과 포지\(forge\) 생태계 전반의 지원 미비 등 실질적인 마이그레이션 과제를 수반한다.

**「영향」** 이 논쟁은 Git 생태계가 SHA-256으로 전환할 때 서브모듈, 포지 지원, 기존 도구 호환성 등 실무적 난제를 어떻게 해결할지에 대한 논의를 촉발했으며, GitHub 같은 대형 호스팅 플랫폼의 지원 로드맵이 전환 속도를 좌우할 가능성이 크다.

**「커뮤니티 반응」** 댓글들은 저자가 SHA-1의 실질적 위협\(SHAttered\)과 충돌 공격의 위험성을 잘못 전달했고 GitHub의 SHA-256 지원 상황도 왜곡했다고 지적하며 기술적 정확성에 강한 의문을 제기했다. 일부는 Fossil SCM이 SHAttered 공개 6일 만에 SHA3-256 지원을 추가한 사례를 대조하며 신속한 대응의 선례로 언급했고, 다른 댓글은 이번 변화가 순수한 보안 문제라기보다 SHA-1 사용을 금지하는 기업·정부 규정에 따른 정치적 요인일 수 있다는 추측을 제시했다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://blog.gitbutler.com/git-3-sha-256">Git 3 . 0 &#x27;s upcoming SHA - 256 default will be a costly mistake</a></li>
<li><a href="https://github.com/romkatv/gitstatus/issues/411">Support SHA-256 repos · Issue #411 · romkatv/gitstatus - GitHub</a></li>
<li><a href="https://lwn.net/Articles/898522/">Whatever happened to SHA-256 support in Git? - LWN.net</a></li>

</ul>
</details>

**태그**: `#git`, `#cryptography`, `#version-control`, `#security`, `#infrastructure`

---

<a id="item-tech-news-9"></a>
### [arXiv, 제출 급증 대응해 월간 및 동시 제출 건수 제한 도입](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) ⭐️ 6.0/10

arXiv는 제출량 급증에 대응해 제출자당 월 2건, 동시 활성 제출 3건으로 제한하는 새로운 rate limit 정책을 발표했다. 2016년 9월 9,869건이던 월간 제출 건수는 2024년 9월 20,569건을 거쳐 2025년 9월에는 40,363건으로 늘어났고, 이로 인해 arXiv 직원과 모더레이터에게 약 9,000건의 지원 티켓이 발생했다. 이번 제한은 저자\(author\) 단위가 아니라 제출자\(submitter\) 단위로 적용되어, 공동저자가 많은 대규모 협업 연구팀은 제출 예산을 더 폭넓게 확보할 수 있는 구조다.

hackernews · 50kIters · 10월 1일 20:12 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49926512)

**「배경」** arXiv는 물리학, 수학, 컴퓨터과학 등 분야의 논문을 동료심사 전 사전공개\(preprint\)하는 무료 공개 저장소로, 연구자들이 빠르게 연구 결과를 공유하고 저널 투고 전 커뮤니티 피드백을 받는 핵심 인프라로 자리잡았다. 최근 AI 및 머신러닝 분야 연구 생산량이 급증하면서 제출량이 자동화된 도구와 결합해 기하급수적으로 늘어나, 소규모 인력으로 운영되던 모더레이션 체계에 과부하가 걸리게 되었다.

**「영향」** 이번 정책으로 개별 연구자나 소규모 팀이 짧은 기간에 다수의 논문을 쏟아내는 관행에는 제약이 생기지만, 대형 협업 그룹은 저자 수에 비례해 상대적으로 여유를 갖게 되어 형평성 문제가 제기될 수 있다. 다만 커뮤니티는 승인 지연\(수주 소요\)과 근본적인 확장성 문제가 이번 제한만으로 해결되지 않을 것이라는 우려도 함께 표하고 있다.

**「커뮤니티 반응」** 일부 학계 이용자는 저자 수에 비례해 제출 예산이 늘어나는 제출자 단위 제한 방식을 공정하다고 평가하며 학회 공동저자 제한 정책에도 이를 적용하길 희망했지만, 다른 이용자는 최근 논문 승인에 18일 이상 걸리는 등 심각한 지연을 겪고 있어 hal.science 같은 대체 저장소로 옮겼다고 밝혔다. 또 다른 댓글들은 이러한 제출 폭증이 자동화\(AI\)로 인해 인간 규모에서 작동하던 공공재가 더 이상 지속 가능하지 않게 되는 현상의 한 사례이며, 근본적으로는 논문 수 기반의 경력 평가 관행 자체가 문제라는 지적도 나왔다.

**태그**: `#arxiv`, `#research-infrastructure`, `#open-science`, `#policy`, `#academic-publishing`

---

<a id="item-tech-news-10"></a>
### [Debian, Linux 커널 다중 취약점 보안 패치 DSA-6528-1 발행](https://news.hada.io/topic?id=34652) ⭐️ 6.0/10

Debian 프로젝트는 Linux 커널의 여러 취약점을 수정하는 DSA-6528-1 보안 공지를 발행했다. 이번에 발견된 취약점들은 권한 상승, 서비스 거부\(DoS\), 정보 유출로 이어질 수 있는 문제들을 포함한다. 안정 배포판 trixie에서는 linux 패키지 6.12.111-1 버전에서 해당 문제들이 수정되었으며, 관련 Debian 버그 번호는 1108860이다. Debian은 사용자들에게 linux 패키지의 즉시 업그레이드를 권고하며, 상세 보안 상태는 Debian 보안 추적기에서, 업데이트 적용 방법은 Debian 보안 안내 페이지에서 확인할 수 있다.

rss · GeekNews · 10월 2일 03:31

**「배경」** Debian Security Advisory\(DSA\)는 Debian 프로젝트가 패키지에서 발견된 보안 취약점과 수정 버전을 공식적으로 공지하는 문서로, DSA-6528-1은 Linux 커널 패키지를 대상으로 한다. Debian의 현재 안정 배포판 코드명인 trixie는 여러 사용자가 운영 환경에서 사용하는 배포판으로, 커널의 권한 상승·서비스 거부·정보 유출 취약점은 시스템 전체의 보안과 안정성에 직접적인 영향을 줄 수 있어 신속한 패치 적용이 권장된다.

**「영향」** Debian trixie를 사용하는 시스템 관리자는 권한 상승이나 정보 유출로 인한 보안 사고를 막기 위해 linux 패키지를 6.12.111-1 버전으로 신속히 업그레이드해야 한다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://lwn.net/Articles/1097401/">Debian alert DSA-6528-1 (kernel) - lwn.net</a></li>
<li><a href="https://linuxsecurity.com/advisories/debian/debian-dsa-6528-1-linux">Debian Linux Critical Privilege Escalation Denial of Service DSA-6528-1</a></li>

</ul>
</details>

**태그**: `#linux-kernel`, `#security-vulnerability`, `#debian`, `#system-security`, `#open-source`

---

<a id="item-tech-news-11"></a>
### [OpenAI, 안전 연구원 3명과 결별…WSJ 보도](https://techcrunch.com/2026/10/01/openai-cuts-ties-with-three-safety-researchers-wsj-reports/) ⭐️ 6.0/10

WSJ 보도에 따르면 OpenAI는 내부 조사 끝에 민감한 회사 정보를 부적절하게 다룬 안전 연구원 3명과의 관계를 끊었다. 해당 연구원들의 구체적인 신원이나 소속 팀, 정보 유출 혹은 오용의 정확한 경위는 아직 공개되지 않았다. 이번 조치는 내부 조사 결과에 따른 것으로, OpenAI 측의 공식 성명이나 추가 세부사항은 보도에 포함되지 않았다.

rss · TechCrunch AI · 10월 1일 18:14

**「배경」** OpenAI는 GPT 시리즈 등 자사 AI 모델의 위험성을 평가하고 안전성을 검증하는 내부 safety 연구 조직을 운영하고 있으며, 소속 연구원들은 미공개 모델 아키텍처와 안전성 평가 자료 등 민감한 정보에 접근할 수 있다. 이번 사안은 이러한 연구원들이 외부의 제3자 AI 안전·감시 단체와 민감 정보를 공유하면서, 독점 기술과 미공개 평가 자료 보호를 위한 비밀유지계약\(NDA\)을 위반했다는 보도와 관련이 있다.

**「영향」** 이번 사건은 대형 AI 랩 내부에서 안전 연구팀이 다루는 민감한 정보에 대한 접근 통제와 보안 관행이 어떻게 이뤄지는지에 대한 외부의 의문을 키울 수 있다. 세부 내용이 공개되지 않아 업계 전반에 미칠 구체적 파장은 현재로서는 불확실하다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.investing.com/news/stock-market-news/openai-fires-three-safety-researchers-for-sharing-sensitive-data-wsj-reports-4927954">OpenAI fires three safety researchers for sharing sensitive data...</a></li>

</ul>
</details>

**태그**: `#openai`, `#ai-safety`, `#organizational-governance`, `#industry-news`

---

<a id="item-tech-news-12"></a>
### [Google, 새 Gemini AI 모델 출시하며 안전 우려로 접근 제한](https://news.google.com/rss/articles/CBMilwFBVV95cUxQeGxacWxBMjBHTEdEel95dW1GOVVOX09PR3laaEVXQXZvNDBRalVNMFNDTmstQUZ2YU1fX19SaHAwZnp1UVdvS2dVeHBPbTBGU1pfYmllWmJoVFozUUZXcDdHQm9kal92dWpCaEtyVndfWFhuVkVQcEk0djRROS1VUEJFa09VOS15M0U1YVZPSHZIWDVqZVZB?oc=5) ⭐️ 6.0/10

Google이 새로운 Gemini AI 모델을 공개했으나, 안전 문제를 이유로 해당 모델에 대한 접근을 제한하고 있다고 The Guardian이 보도했다. 보도된 내용은 헤드라인 수준으로, 구체적인 모델 버전명, 공개 범위, 제한 방식, 안전 우려의 구체적 내용 등은 아직 확인되지 않았다. 따라서 이번 모델이 기존 Gemini 라인업과 어떻게 다른지, 어떤 기능이나 사용자층에 제한이 적용되는지는 추가 정보가 필요하다.

google\_news · The Guardian · 10월 1일 16:57

**「배경」** Google은 최신 프론티어 모델 Gemini 4 Argon을 공개했지만, 해커에 의한 악용 가능성을 우려해 일반 공개 대신 검증된 사이버보안 전문가 그룹에만 단계적으로 접근을 허용하고 있다. 이는 미국 정부와의 사전 출시 안전성 평가 협력의 일환으로, Anthropic이 지난 6월 Claude Mythos와 Claude Fable 모델에 대해 워싱턴의 요청으로 접근을 일시 중단했던 사례 이후 마련된 강력한 AI 모델 사전 검증을 위한 자발적 절차와 맥락을 같이한다.

**「영향」** 접근 제한의 구체적 범위가 공개되지 않아, 개발자나 일반 사용자가 실제로 어떤 기능 손실을 겪을지는 불확실하다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/oct/01/google-releases-gemini-model-restrictions">Google rolls out new Gemini AI model but restricts ... | The Guardian</a></li>
<li><a href="https://uk.finance.yahoo.com/news/google-restricts-access-ai-model-211124931.html">Google restricts access to new AI model over safety concerns</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model</a></li>

</ul>
</details>

**태그**: `#gemini`, `#model-updates`, `#ai-safety`, `#google-ai`, `#access-restrictions`

---

<a id="item-tech-news-13"></a>
### [Apollo, 일본 150억 달러 규모 AI 인프라 프로젝트 지원](https://news.google.com/rss/articles/CBMigAFBVV95cUxNN2VZend0VVN1dkFiYzZFNDlHc0xfV01zSWNMdU5FZkxpUWRJR05wSUFpMy0yYm5admtzZGoza3JRS1lLSnQ3TW5xTDdlSWdpSmlpdktKRE9ZeHpHUDZ0TlU4QnMtUkFoa3JaeklITHlhQVMyV1BHT3ZkRUZDaVFibg?oc=5) ⭐️ 6.0/10

글로벌 자산운용사 Apollo가 일본에서 진행되는 150억 달러 규모의 AI 인프라 프로젝트를 지원하기로 했다. 현재까지 공개된 내용으로는 구체적인 데이터센터 위치, 참여 파트너사, 자금 집행 일정 등 세부 사항은 확인되지 않는다. 다만 이번 결정은 Apollo를 비롯한 대형 투자기관들이 AI 수요 증가에 대응해 아시아 지역 인프라에 대규모 자본을 투입하고 있는 최근 흐름을 보여주는 사례다.

google\_news · The Japan Times · 10월 2일 02:30

**「배경」** Apollo Global Management는 사모 자산 운용사로서 최근 데이터센터 등 AI 인프라에 대한 대규모 자금 조달에 적극적으로 나서고 있으며, 이번 건은 그러한 전략의 일환이다. 전 세계적으로 생성형 AI 수요 증가에 따라 대규모 데이터센터와 컴퓨팅 인프라 구축을 위한 조 단위 투자가 미국과 아시아 각지에서 활발히 이뤄지고 있다.

**「영향」** 이번 투자는 미국과 중국에 비해 데이터센터 용량이 뒤처진 일본의 AI 인프라 확충을 가속화하며, JERA\(부지·전력\), Dell\(하드웨어\), RHAELM\(개발·운영\)으로 구성된 컨소시엄이 아시아 최대 규모로 거론되는 치바 데이터센터를 구축하는 데 핵심 자금을 제공한다. Apollo로서는 AI 인프라 분야 투자 노출을 확대하는 사례로, 글로벌 사모펀드 자본이 아시아 AI 데이터센터 구축에 본격적으로 유입되는 흐름을 보여준다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-10-01/apollo-to-support-15-billion-ai-infrastructure-project-in-japan">Apollo to Back $ 15 Billion Japan AI Infrastructure Project</a></li>
<li><a href="https://theoutpost.ai/news-story/jera-dell-partner-on-15-billion-ai-infrastructure-project-to-build-asia-s-largest-data-centre-31578/">JERA, Dell Partner on $15B AI Infrastructure in Japan</a></li>
<li><a href="https://www.cryptopolitan.com/japan-apollo-backs-ai-build-jera-plant/">Japan &#x27;s power, Wall Street&#x27;s compute: Apollo backs $15B AI build...</a></li>

</ul>
</details>

**태그**: `#ai-infrastructure`, `#investment`, `#japan`, `#generative-ai`

---

## 심층 분석 · 뉴스레터

<a id="item-tech-blog-1"></a>
### [RLM과 에이전트 하네스: Alex Zhang가 말하는 학계의 위험한 베팅](https://www.latent.space/p/rlm) ⭐️ 6.0/10

rss · Latent Space · 10월 2일 00:28

**「배경」** Claude Code, Codex, Pi 같은 현재 에이전트 시스템들은 겉보기엔 다르지만, Alex Zhang에 따르면 구조적으로는 거의 동일하다. 모두 이전 궤적을 프롬프트에 계속 이어붙이는 방식이라서, 모델이 특별히 학습되지 않은 긴 맥락이나 낯선 과제에서는 쉽게 분포 밖\(out-of-distribution\) 상황에 빠진다는 한계가 있다.

**「방안」** MIT 박사과정생 Alex Zhang은 이 문제를 Recursive Language Models\(RLM\)라는 하네스 설계로 접근한다. 핵심 아이디어는 전체 과제 자체는 모델이 본 적 없는 낯선 문제라도, 하네스가 이를 하위 문제를 다루는 서브에이전트 호출들로 쪼개면 각 개별 LM 호출은 '지역적으로는' 익숙한 분포 안에 머무를 수 있다는 것이다. 그는 이를 context offloading, 코드 실행, 재귀적 서브에이전트 호출, 공유 메모리 같은 메커니즘으로 구현했다고 설명한다. 이 원칙은 Prime Intellect와 협업한 Prime Agent 프로젝트로 이어졌는데, IPython만을 유일한 도구로 제한하고 나머지 기능은 Python/Bash 모듈로 호출하게 하는 '지속형\(continual\) 하네스' 구조를 가진다. Zhang은 RLM 기반 하네스가 OpenAI의 Astra보다 먼저 ARC-AGI-3를 사실상 해결했다고 언급하지만, 구체적 수치나 검증 자료는 제시하지 않는다. 대화는 또한 OpenAI가 시도했다는 수만 개 에이전트·수백억 토큰 규모의 멀티에이전트 실험과, 그런 거대 스웜에서도 수렴\(convergence\)이 여전히 어려워 탐색의 상당 부분이 낭비될 수 있다는 미해결 문제를 짚는다. 다만 전체 논의는 구체적 벤치마크 결과보다는 연구 철학과 가설 수준의 대화에 가깝다는 점이 한계로 지적된다.

**「요점」** Zhang의 핵심 주장은, 모델 자체의 성능보다 하네스\(harness\) 설계가 아직 활용되지 않은 큰 능력치를 가두고 있으며, 미래의 '언어모델'은 단일 디코더가 아니라 보이지 않는 에이전트 스웜일 수 있다는 것이다. 그는 이런 구조적 질문이야말로 산업 연구소가 피하는, 하지만 박사과정생이 과감히 베팅해볼 만한 영역이라고 말한다.

**태그**: `#large-language-models`, `#generative-ai`, `#agent-systems`, `#research-methodology`, `#gpu-optimization`

---