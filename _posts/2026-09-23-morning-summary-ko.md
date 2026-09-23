---
layout: default
title: "AI 브리핑 · 2026-09-23 아침"
report_id: "2026-09-23-morning"
date: 2026-09-23
lang: ko
---

> 수집한 160건 중 17건을 골랐습니다.

---

**업계 동향**
1. [OpenAI, GPT-6 Sol과 Luna 변형 모델 출시](#item-tech-news-1) ⭐️ 8.0/10
2. [WordPress 인증 없는 경로 순회 취약점, 조건부 RCE로 이어져](#item-tech-news-2) ⭐️ 8.0/10
3. [Trail of Bits, SAML의 XML 기반 설계 결함을 근본 문제로 지적](#item-tech-news-3) ⭐️ 7.0/10
4. [펜타곤, 이란 학교 오폭에 AI 과잉 의존 영향 인정](#item-tech-news-4) ⭐️ 7.0/10
5. [Filament: DB와 SaaS 데이터를 복제·동기화하는 오픈소스 엔진](#item-tech-news-5) ⭐️ 7.0/10
6. [Meta Muse AI에 파일시스템 요청하자 내부 파일 6.8GB 노출](#item-tech-news-6) ⭐️ 7.0/10
7. [US criticises Australia's proposed algorithm opt-out laws as 'censorship'](#item-tech-news-7) ⭐️ 6.0/10
8. [2007년 단종된 FoxPro, Rust와 WebAssembly로 되살아나다](#item-tech-news-8) ⭐️ 6.0/10
9. [Unreal Agent: 도구 호출 최적화에 초점 맞춘 오픈소스 LLM 에이전트 프레임워크](#item-tech-news-9) ⭐️ 6.0/10
10. [GrapheneOS, Motorola와 공식 파트너십…2027년 사전설치 기기 출시 예고](#item-tech-news-10) ⭐️ 6.0/10
11. [Qualcomm, AI 강화한 신형 스마트폰 칩 두 종 출시](#item-tech-news-11) ⭐️ 6.0/10
12. [Meta, AI 어시스턴트 Muse가 OpenClaw를 모방했다고 인정](#item-tech-news-12) ⭐️ 6.0/10
13. [Anthropic·OpenAI 신모델, 성능 조금 향상시키고 가격은 대폭 인하](#item-tech-news-13) ⭐️ 6.0/10
14. [Microsoft, 12,000개 계정 침해한 AI 공격 플랫폼 'EvilTokens' 차단](#item-tech-news-14) ⭐️ 6.0/10
15. [AntLing, UI/UX 디자인 특화 6B 오픈소스 이미지 모델 Ming-Image 공개](#item-tech-news-15) ⭐️ 6.0/10

**심층 분석 · 뉴스레터**
1. [John Platt가 말하는 Google ERA와 AI 기반 과학 연구](#item-tech-blog-1) ⭐️ 7.0/10
2. [Claude Opus 5.5와 GPT-6 Sol/Luna, 가격 전쟁의 새 국면](#item-tech-blog-2) ⭐️ 7.0/10

---

## 업계 동향

<a id="item-tech-news-1"></a>
### [OpenAI, GPT-6 Sol과 Luna 변형 모델 출시](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 8.0/10

OpenAI가 GPT-6의 새로운 변형 모델인 Sol과 Luna를 공개했다. 가장 주목할 점은 GPT-6 Luna의 가격이 이전 세대인 GPT-5.6 Luna 대비 절반 수준으로 책정되었다는 것이다. 커뮤니티에서는 두 모델의 실제 성능과 사용 경험을 비교하는 반응이 이어졌으며, 특히 코딩 및 에이전트 작업에서의 체감 성능과 요금제별 사용량 한도가 실질적인 관심사로 떠올랐다.

hackernews · OpenAI · 9월 22일 18:00 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49805509)

**「배경」** OpenAI는 앞서 GPT-6 Astra라는 최상위 모델을 출시한 바 있으며, 이번 Sol과 Luna는 Astra의 기술적 발전을 바탕으로 하되 속도와 비용 효율성에 초점을 맞춘 하위 라인업이다. 기존에는 GPT-5.6 세대에서 Sol과 Luna라는 명칭의 모델이 존재했으며, 이번 발표는 이를 GPT-6 세대로 갱신하는 것이다. OpenAI의 모델 계보에서 Astra, Sol, Luna와 같은 이름은 동일 세대 내에서 성능과 비용의 균형점이 다른 여러 변형을 구분하는 방식으로 사용된다.

**「영향」** GPT-6 Luna의 가격 인하는 비용에 민감한 개발자와 기업 사용자들이 LLM 기반 도구를 선택할 때 가격 대비 성능을 재평가하게 만드는 요인이 될 수 있다.

**「커뮤니티 반응」** 일부 사용자는 이전 모델\(5.6 Sol\)의 소통 방식과 작업 궁합에 애착을 느껴 새 모델로의 전환에 대한 아쉬움을 표하는 한편, 다른 사용자들은 Codex Pro와 Claude Code 같은 경쟁 도구 대비 사용량 한도와 요금제 구조를 비교하며 실무적 선택 기준을 논의했다. 일반 사용자 관점에서는 ChatGPT Plus가 일상적인 작업에서 이미 충분히 만족스럽다는 긍정적 평가도 나왔다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna/1399925">Announcing GPT - 6 Sol and GPT - 6 Luna - Announcements ...</a></li>

</ul>
</details>

**태그**: `#large-language-models`, `#model-updates`, `#pricing`, `#openai`, `#generative-ai`

---

<a id="item-tech-news-2"></a>
### [WordPress 인증 없는 경로 순회 취약점, 조건부 RCE로 이어져](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 8.0/10

WordPress의 get\_page\_template\(\) 함수에서 인증되지 않은 공격자가 활성 테마 디렉터리 밖의 읽기 가능한 로컬 .php 파일을 포함시킬 수 있는 경로 순회 취약점이 발견됐다. 이 취약점이 원격 코드 실행\(RCE\)으로 이어지려면 부모 또는 자식 테마 최상위에 page-로 시작하는 디렉터리가 존재해야 하며\(Twenty Twelve, Twenty Fourteen, Neve, Hestia, Sydney 등의 테마가 해당\), 서버에 읽기 가능한 대상 PHP 파일이 있어야 하는 등 추가 조건이 충족되어야 한다. 예시로 register\_argc\_argv=On 환경에서 pearcmd.php를 이용한 공격 경로가 제시됐다. 해당 취약점은 WordPress 7.1.2에서 수정됐으며, 이전 버전 사용자를 위해 4.7까지의 모든 브랜치에 백포트됐다.

hackernews · vntok · 9월 22일 16:33 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49803959)

**「배경」** locate\_template\(\)과 get\_page\_template\(\)은 WordPress가 테마 파일을 찾아 로드할 때 사용하는 핵심 함수로, 페이지 슬러그나 템플릿 이름을 바탕으로 파일 경로를 조합한다. 이미 9년 전 공식 문서의 사용자 코멘트에서 locate\_template\(\)이 디렉터리 순회를 방지하지 않는다는 점이 지적된 바 있어, 이번 취약점은 오래전부터 잠재해 있던 설계상의 결함으로 볼 수 있다.

**「영향」** 이 취약점은 인증 없이 공격 가능하고 특정 테마와 서버 환경 조건이 맞을 경우 RCE로 확대될 수 있어, 패치가 적용되지 않은 수백만 개의 WordPress 사이트가 위험에 노출된다. 코멘트에 따르면 전체 설치의 약 1/3이 최신 7 브랜치를 사용하지 않고 있어, 백포트된 패치의 신속한 적용이 실제 피해 규모를 좌우할 것으로 보인다.

**「커뮤니티 반응」** 일부 개발자는 WordPress가 웹 역사상 가장 많이 악용된 소프트웨어 중 하나라며 비판적인 반응을 보였고, 이번 사태를 계기로 Hugo 같은 정적 사이트로 이전해 안도감을 느꼈다는 경험담도 공유됐다. 다른 댓글은 9년 전 문서 코멘트가 이번 취약점의 본질과 해결책을 정확히 예견했다는 점을 아이러니하게 지적했으며, 실제 패치 커밋 링크도 공유됐다.

**태그**: `#wordpress`, `#security-vulnerability`, `#rce`, `#path-traversal`, `#web-infrastructure`

---

<a id="item-tech-news-3"></a>
### [Trail of Bits, SAML의 XML 기반 설계 결함을 근본 문제로 지적](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/) ⭐️ 7.0/10

Trail of Bits는 블로그 글에서 SAML이 XML 기반 설계 자체에서 비롯된 구조적 결함으로 인해 보안 취약점을 반복적으로 낳는다고 분석했다. 커뮤니티 댓글에서는 널리 쓰이는 C 구현체 xmlsig가 기본 설정에서 공개키 서명 검증 외에도 공격자가 문서에 지정한 비밀번호로 HMAC 검증을 수행하거나, 웹 PKI를 통해 공격자 자신의 TLS 인증서로 서명한 SAML 문서를 유효한 것으로 인정해버리는 사례가 구체적으로 언급되었다. 이는 XML 서명 검증 로직이 지나치게 유연하게 설계되어 공격자가 검증 방식 자체를 조작할 수 있었음을 보여주는 사례다. 분석은 이런 문제들이 SAML이 인증이라는 목적에 맞지 않게 마크업 언어와 문서 서명이라는 도구를 억지로 끌어다 쓴 결과라는 비판으로 이어진다.

hackernews · aray07 · 9월 22일 18:57 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49806335)

**「배경」** SAML\(Security Assertion Markup Language\)은 XML 기반으로 신원 제공자\(IdP\)와 서비스 제공자\(SP\) 간에 인증·인가 정보를 교환하기 위해 2000년대 초 제정된 엔터프라이즈 SSO 표준이다. XML 문서에 전자서명을 적용하는 XML Signature\(xmlsig\) 방식으로 무결성을 보장하는데, 이 서명 검증 로직의 복잡성이 여러 구현 취약점의 근원이 되어왔다. OIDC\(OpenID Connect\)는 OAuth2 위에 구축된 비교적 최신 프로토콜로, JSON과 JWT를 사용해 SAML보다 단순한 인증 흐름을 제공하며 SAML의 대안으로 자주 언급된다.

**「영향」** SAML을 SSO 수단으로 채택한 기업과 제품은 XML 서명 검증 로직의 설계 결함으로 인한 잠재적 취약점을 계속 안고 갈 수밖에 없으며, 이는 라이브러리 구현 방식에 따라 심각한 인증 우회로 이어질 수 있다.

**「커뮤니티 반응」** 댓글에서는 OIDC가 OAuth2의 인가\(authorization\) 개념 위에 세워져 있어 순수한 인증 용도로는 한계가 있다는 지적과, SAML은 IdP 주도 흐름 같은 엔터프라이즈 SSO 특화 기능을 여전히 갖추고 있어 완전히 대체되기 어렵다는 실무적 의견이 제시됐다. 일부는 SAML의 문제를 XML을 만능 도구로 여기던 시대의 산물로 보면서도, OIDC 역시 구현체 간 일관성 부족과 Google 등 특정 사업자 중심의 가정이 남아 있어 완전한 해법은 아니라고 지적했다.

**태그**: `#authentication`, `#saml`, `#security-vulnerabilities`, `#xml`, `#identity-management`

---

<a id="item-tech-news-4"></a>
### [펜타곤, 이란 학교 오폭에 AI 과잉 의존 영향 인정](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 7.0/10

펜타곤 보고서는 이란 학교 공습 사건에서 AI에 대한 과도한 의존이 기여 요인이었다고 밝혔다. Maven 시스템은 구식 데이터로 인해 Minab 소재 건물을 이슬람혁명수비대\(IRGC\) 시설로 잘못 분류해 1일차 권장 공격 목표로 산출했으며, 이 건물은 실제로는 학교였다. 과거 수 시간이 걸리던 목표 선정 작업이 수 분으로 단축되면서 충분한 검증 절차 없이 공격이 승인되었다. 보고서는 미국이 민간 시설을 타격할 상당한 위험을 인지하고도 이를 검증할 의무를 다하지 못했으며 이는 단순 과실을 넘어선다고 결론지었다.

hackernews · devonnull · 9월 22일 19:03 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49806430)

**「Maven Smart System과 AI 기반 표적 선정」** Maven Smart System은 미군이 위성·정찰 영상을 분석해 공격 표적 후보를 자동 식별하도록 개발한 AI 기반 표적 선정 시스템이다. Military Times 보도에 따르면 Maven은 전체 조건에서 약 60%의 물체 식별 정확도를 보이는데, 이는 인간 분석가의 84%보다 낮으며 악천후나 시야가 나쁜 환경에서는 정확도가 30% 미만으로 떨어진다. 이번 사건은 이란 공습 작전 첫 24시간 동안 1,000개 이상의 표적이 타격되는 빠른 작전 템포 속에서 발생했으며, 미 하원 민주당 의원 120여 명이 Maven의 역할에 대해 국방장관에게 공식 질의했으나 펜타곤은 조사가 진행 중이라는 이유로 공개 답변을 하지 않은 상태다.

**「군사 AI 목표 선정 체계에 대한 신뢰 위기」** 이번 사건은 Maven과 같은 AI 기반 목표 선정 시스템이 실전 배치된 상태에서 구식 데이터와 검증 부족이 결합될 경우 민간인 피해로 직결될 수 있음을 공식적으로 입증한 사례로, 향후 미군의 AI 목표 선정 절차와 인간 검토 단계에 대한 규정 강화 압력이 커질 것으로 보인다. 또한 유사한 오인 사례\(중국 선박 오판 등\)와 함께 언급되면서 군사 AI 도입 속도를 늦추고 인간 개입 기준을 명문화해야 한다는 의회 및 감시 단체의 요구가 힘을 받을 가능성이 있다.

**「커뮤니티 반응」** 일부 댓글은 보고서 인용문을 근거로 실제 문제는 AI 자체가 아니라 무모하게 검증을 생략한 의사결정과 지휘 책임이라고 지적했다. 다른 참여자들은 무인 로봇의 공격 명령 수용, 핵물질 운반 선박으로 오인된 중국 선박 사건 등 유사 사례를 언급하며 속도 최적화가 검증을 희생시키는 구조적 문제를 우려했다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.bloomberg.com/graphics/2026-iran-school-attack/">Inside US Military ‘Kill Chain’ That Destroyed an Iranian School</a></li>
<li><a href="https://www.militarytimes.com/news/your-military/2026/03/24/deadly-iran-school-strike-casts-shadow-over-pentagons-ai-targeting-push/">Deadly Iran school strike casts shadow over Pentagon’s AI targeting push</a></li>
<li><a href="https://www.ibtimes.co.uk/pentagon-review-ai-failures-iran-school-strike-1820787">Pentagon Blames AI System for Deadly US Strike That Killed 123 Iranian Schoolchildren | IBTimes UK</a></li>
<li><a href="https://www.objectivist.co/2026/09/ai-targeting-may-outrun-human-control-before-disaster-strikes/">AI Targeting May Outrun Human Control Before Disaster Strikes</a></li>
<li><a href="https://edition.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship">Exclusive: US military had close call after using AI for false intelligence...</a></li>

</ul>
</details>

**태그**: `#ai-safety`, `#military-systems`, `#automation-bias`, `#decision-making`, `#real-world-impact`

---

<a id="item-tech-news-5"></a>
### [Filament: DB와 SaaS 데이터를 복제·동기화하는 오픈소스 엔진](https://news.hada.io/topic?id=34152) ⭐️ 7.0/10

Filament는 Go로 작성된 오픈소스 데이터 복제 엔진으로, PostgreSQL/MySQL 같은 데이터베이스뿐 아니라 GitHub, Slack, Notion, Stripe, HubSpot 등 SaaS 서비스의 데이터를 ClickHouse, Snowflake, BigQuery, Redshift, Iceberg, S3/GCS 등 다양한 대상으로 옮기고 동기화한다. 전체 복사, 변경분만 가져오기, 변경 데이터 캡처\(CDC\) 방식을 지원하며, 데이터를 일정 크기로 나눠 처리하면서 체크포인트를 남겨 중단 시 처음부터 다시 복사하지 않고 재개할 수 있다. 전송 과정에서는 체크섬 비교로 값과 순서 변경 여부를 검사하지만, 모든 저장소를 다시 읽어 검증하거나 중복을 완전히 방지하지는 않는다. 웹 UI에서 소스와 대상을 연결하고 복제 방식·일정을 설정할 수 있으며, 동일한 기능을 API로도 호출할 수 있어 자동화가 가능하다. 독립 실행 파일 운영이나 Go 애플리케이션 내장, Kubernetes/Helm 배포를 지원하며 Apache-2.0 라이선스로 공개되어 있다.

rss · GeekNews · 9월 23일 00:40

**「배경 지식」** 데이터 복제\(replication\) 도구는 여러 데이터베이스나 SaaS 서비스에 흩어진 데이터를 데이터 웨어하우스나 다른 저장소로 통합하는 데 사용되며, ETL/ELT 파이프라인 구축의 핵심 구성요소다. 변경 데이터 캡처\(CDC\)는 원본 데이터의 삽입/수정/삭제 이벤트만 추적해 전체 재복사 없이 최신 상태를 유지하는 기법으로, 대용량 데이터를 다룰 때 효율성과 실시간성을 높여준다. Filament는 이러한 복제 작업을 Go로 구현한 오픈소스 엔진으로, GitHub 저장소\(galaxy-io/filament\)를 통해 공개되어 있다.

**「영향」** 여러 SaaS와 데이터베이스에 흩어진 데이터를 하나의 웨어하우스나 스토리지로 통합해야 하는 엔지니어링 팀이 상용 ETL 서비스 대신 자체 호스팅 가능한 오픈소스 대안을 확보하게 됐다. 다만 완전한 중복 방지나 전체 재검증 기능은 제공하지 않으므로, 데이터 정합성이 엄격히 요구되는 파이프라인에는 추가 검증 로직이 필요할 수 있다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://github.com/galaxy-io/filament">GitHub - galaxy-io/filament: Pluggable data replication with checkpointing, batching, and integrity events · GitHub</a></li>
<li><a href="https://deepwiki.com/galaxy-io/filament">galaxy-io/filament | DeepWiki</a></li>

</ul>
</details>

**태그**: `#open-source`, `#data-integration`, `#database-tools`, `#etl-pipeline`, `#go`

---

<a id="item-tech-news-6"></a>
### [Meta Muse AI에 파일시스템 요청하자 내부 파일 6.8GB 노출](https://news.hada.io/topic?id=34136) ⭐️ 7.0/10

보안 연구자가 Meta의 Muse AI 어시스턴트에게 접근 가능한 파일을 압축해 Google Drive로 보내 달라고 요청하자 실제로 내보내기가 이루어졌으며, 압축 상태 약 2.7GB, 해제 후 약 6.8GB의 데이터가 전송되었다. 여기에는 세션에 할당된 Linux 실행 환경의 Ubuntu 시스템 파일, Hatch라는 내부 런타임 문서\(SOUL.md, MEMORY.md, TOOLS.md 등\), 약 68개 스킬 구현체, React/TypeScript 기반 Spaces 앱 프레임워크, Postgres 기반 메모리 검색 로직\(memory.entries, memory.embeddings, memory.claims\), 매시간 실행되는 대조 작업과 야간 'dream' 검토를 통한 지침 갱신 메커니즘, ESP32-C5 기반 실험적 Home Link 가정용 기기 통합 문서, 그리고 SSH 키 파일까지 포함되어 있었다. Muse는 실제로 Codex CLI 0.149.0을 보유하고 있었지만 코딩 에이전트로 쓰인 증거는 없었고, 대신 Codex에 포함된 bubblewrap 샌드박스로 ffmpeg/ffprobe 작업을 nobody 권한으로 격리해 실행하는 것으로 확인되었다. 연구자는 컨테이너 탈출을 제한적으로 시도했으나 경계는 유지되는 것으로 보였고, 발견한 80개 소켓에 대한 추가 탐색은 운영 중인 시스템이라는 점과 자신의 경험 부족을 이유로 중단했다. Meta에 버그 바운티로 신고했으나 회사는 이를 'Not Applicable'로 처리했으며, 어떤 사유가 적용되었는지는 명시하지 않고 보안·개인정보 영향에 대한 추가 증거만 요청했다.

rss · GeekNews · 9월 22일 17:49

**「Muse와 Hatch 런타임 배경」** Muse는 Meta가 최근 공개한 개인용 AI 에이전트로, 브라우저 사용, 결제, 파일 생성 등 다양한 작업을 대신 수행할 수 있도록 설계됐다. Meta는 내부적으로 이 시스템을 Hatch라 부르며, 각 세션에 systemd-nspawn 기반의 격리된 컨테이너\(런타임 셀\)를 할당해 실행되는 바이너리와 도구들을 통제한다고 밝힌 바 있다. 이번 사례는 사용자가 Muse에게 파일시스템 접근 가능 자료를 압축해 전송해 달라고 요청했을 때, 이러한 격리 컨테이너 내부의 시스템 파일과 내부 문서, 코드가 그대로 외부로 노출된 정보 공개 취약점을 다룬다.

**「영향」** Muse 사용자와 Meta 내부 개발자에게는 세션 격리가 완전하지 않을 수 있다는 신호로, SSH 키와 내부 런타임 구조\(Spaces 프레임워크, 스킬 구현, 메모리 관리 로직\)가 외부에 노출될 위험이 실제로 존재함을 보여준다. Meta가 이를 버그 바운티 대상에서 제외해 공식적인 보안 결함으로 인정하지 않았기 때문에, 유사한 정보 노출 경로가 계속 방치될 가능성이 있으며 다른 AI 에이전트 서비스 운영자들에게도 세션 환경과 대화 기반 파일 내보내기 기능의 경계 설정을 재검토할 필요성을 제기한다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>
<li><a href="https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse">How We Built Safety Into Muse | Meta AI Research</a></li>
<li><a href="https://memedata.com/post/147297">I asked Meta’s Muse for its filesystem and it sent me 6.8GB</a></li>
<li><a href="https://mouse.dev/blog/muse-runtime-export/">I asked Meta’s Muse for its filesystem and it sent me 6.8 GB | Mouse</a></li>

</ul>
</details>

**태그**: `#ai-security`, `#information-disclosure`, `#generative-ai`, `#trust-and-verification`, `#vulnerability`

---

<a id="item-tech-news-7"></a>
### [US criticises Australia's proposed algorithm opt-out laws as 'censorship'](https://www.bbc.com/news/articles/cqj3dgy8x3vro) ⭐️ 6.0/10

호주의 알고리즘 옵트아웃 법안에 대해 미국이 '검열'이라고 비판했다는 보도인데, 커뮤니티 논의에 따르면 기사가 두 가지를 혼동하고 있다. 실제 쟁점은 플랫폼이 '해로운 콘텐츠'를 사전에 제거하도록 요구하는 조항에서 '해로움'과 '위험'의 정의가 불명확하다는 점이다. 이는 표현의 자유와 콘텐츠 규제 사이의 근본적인 긴장을 드러내며, 알고리즘 투명성과 정부 권한의 범위를 둘러싼 국제적 규제 논쟁을 반영한다.

hackernews · 1659447091 · 9월 23일 02:13 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49810829)

**태그**: `#algorithmic-regulation`, `#content-moderation`, `#policy`, `#free-speech`, `#platform-governance`

---

<a id="item-tech-news-8"></a>
### [2007년 단종된 FoxPro, Rust와 WebAssembly로 되살아나다](https://foxscript.org/) ⭐️ 6.0/10

Microsoft가 2007년 버전 9를 끝으로 개발을 중단한 Visual FoxPro를 위해, 동일한 언어를 Rust로 작성하고 WebAssembly로 컴파일한 새 런타임이 공개되었다. 이 프로젝트는 실제 vfp9.exe와 동작을 대조 검증했으며, 기존 2GB 한계를 넘는 테이블 지원, 기존 32비트 .fll 애드인과의 로딩 호환성, 그리고 lambda, JSON, HTTP 서버 같은 현대적 기능을 추가했다. 한 고객사가 20년 된 업무 애플리케이션을 계속 운영하고 싶어 하면서 시작된 프로젝트로, 라이선스는 MIT이다. 다만 보고서\(reports\) 기능은 아직 완성되지 않았고 빌드에는 서명이 되어 있지 않아 초기 단계임을 보여준다.

hackernews · boredjohnny · 9월 22일 21:00 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49808023)

**「배경」** Visual FoxPro는 1980~90년대에 인기를 끈 데이터베이스 기반 개발 환경으로, Microsoft가 인수 후 유지보수하다가 2007년 버전 9를 마지막으로 공식 지원을 종료했다. 그럼에도 니치 산업 분야에서 오래된 32비트 애플리케이션이 여전히 운영 중이며, 이런 레거시 시스템을 재작성하는 비용과 위험이 커서 기존 코드를 그대로 유지하려는 수요가 존재한다.

**「영향」** 여전히 32비트 FoxPro 애플리케이션에 의존하는 니치 산업\(합산 연매출 20억 달러 이상으로 추정\)의 조직들에게 기존 코드와 애드인을 유지하면서 현대적 인프라로 이전할 수 있는 실질적 경로가 열릴 수 있다. 다만 프로젝트가 초기 단계이고 빌드가 서명되지 않았으며, FoxPro의 근본적인 DBC\(Database Container\) 보안 설계 결함은 여전히 해결되지 않은 상태다.

**「커뮤니티 반응」** 일부 댓글은 특정 니치 산업에서 FoxPro 기반 프로그램이 코로나19 이전부터 2026년 현재까지 계속 사용되고 있으며 해당 업계 합산 매출이 20억 달러를 넘는다는 실제 경험을 공유했다. 반면 다른 댓글은 DBC의 저장 프로시저가 권한 체계 없이 평문으로 저장되어 Win32 호출까지 실행 가능한 구조적 보안 취약점을 지적했고, 또 다른 참가자는 과거 물리치료 클리닉에서 파일 잠금 문제로 고생하다 .NET 기반 클라이언트/서버 구조로 전환한 경험을 언급하며 근본적 한계를 우려했다.

**태그**: `#legacy-software`, `#rust`, `#webassembly`, `#database-systems`, `#software-modernization`

---

<a id="item-tech-news-9"></a>
### [Unreal Agent: 도구 호출 최적화에 초점 맞춘 오픈소스 LLM 에이전트 프레임워크](https://unreallabs.ai/blog/unreal-agent/) ⭐️ 6.0/10

Unreal Agent는 GitHub\(unreallabsai/unreal-agent\)에 공개된 오픈소스 LLM 에이전트 프레임워크로, 도구 호출\(tool-calling\) 과정의 토큰 사용량과 모델 턴 수를 줄이는 데 중점을 둔다. 공개된 벤치마크 그래프는 Unreal Agent 하네스가 Astra xhigh 모델로 OpenAI Codex\(Astra max 모델 사용\)와 비슷한 결과를 더 적은 모델 턴과 더 적은 입력 토큰으로 달성한다고 주장한다. 다만 이 비교는 서로 다른 모델 등급\(xhigh 대 max\)을 사용한 것이어서 공정성 문제가 커뮤니티에서 즉시 제기되었다. 프로젝트 설명 문구 자체도 “표면적으로는\(on the surface\)” 동일한 결과를 낸다고 조심스럽게 표현하고 있어, 제작자 스스로도 비교의 한계를 인지하고 있음을 시사한다.

hackernews · trollied · 9월 22일 18:15 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49805748)

**「배경」** LLM 에이전트는 코드 실행, 파일 검색, API 호출 등 다양한 외부 도구\(tool\)를 스스로 선택해 호출하며 작업을 수행하는데, 도구 목록이 많아질수록 컨텍스트가 오염되고 토큰 비용과 지연 시간이 늘어나는 문제가 있다. OpenAI의 Codex는 대표적인 코딩 에이전트 하네스로, 작업 상태를 반복적으로 폴링\(polling\)하는 방식 때문에 토큰 소모가 크다는 지적을 받아왔으며 최근 비동기 도구 호출 지원이 추가되고 있다.

**「영향」** 자체 호스팅 모델을 사용하는 개발자들에게는 토큰 절약을 위한 최적화가 오히려 결과 품질을 낮추는 역효과를 낼 수 있다는 비판이 나왔는데, 이는 API 비용이 들지 않는 환경에서는 토큰 효율성보다 100만 토큰급 대형 컨텍스트 창을 충분히 활용하는 것이 더 중요하다는 지적이다.

**「커뮤니티 반응」** 일부 참여자는 대규모 도구 목록에서 필요한 도구를 계층적으로 찾아가는 프랙탈 도구 발견\(fractal tool discovery\)이나 스플레이 트리\(splay tree\) 같은 자료구조 활용 등 기술적 아이디어를 제안했고, 다른 참여자들은 벤치마크에서 서로 다른 모델 등급을 비교한 점과 “표면적으로”라는 표현에 담긴 한계를 지적했다. 또한 Epic Games의 Unreal Engine과의 상표권 충돌 가능성, 그리고 자체 호스팅 환경에서 비용 최적화가 오히려 성능을 희생시키는 안티패턴이라는 반론도 제기되었다.

**태그**: `#ai-agents`, `#open-source`, `#tool-calling`, `#llm-optimization`, `#generative-ai`

---

<a id="item-tech-news-10"></a>
### [GrapheneOS, Motorola와 공식 파트너십…2027년 사전설치 기기 출시 예고](https://grapheneos.social/@GrapheneOS/117299954135808210) ⭐️ 6.0/10

GrapheneOS 팀은 Motorola Mobility\(Lenovo\)와 공식 파트너십을 체결했으며, 2027년 출시될 고급 플래그십 기기에 GrapheneOS가 사전설치되어 판매될 가능성이 높다고 밝혔다. 이 파트너십은 하드웨어 개선뿐 아니라 GrapheneOS 포팅 작업 지원까지 포함하며, Motorola는 GrapheneOS가 요구하는 업데이트 및 보안 기능 요건을 모두 충족하도록 기기를 개선하고 있다. 지원 범위는 장기적으로 다른 기기, 특히 요구 조건을 충족하는 저가형 기기까지 확대될 계획이다. 커뮤니티 논의에 따르면 실제 사전설치 판매는 Motorola가 직접 하기보다는 Motorola가 기기를 제공하는 제3의 업체를 통해 이루어질 가능성이 있으며, Pixel 기기처럼 웹사이트를 통한 사용자 직접 설치 방식도 계속 제공될 것으로 보인다.

hackernews · Cider9986 · 9월 22일 17:12 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49804683)

**「배경」** GrapheneOS는 Google Pixel 기기에 주로 설치되는 하드웨어 보안 강화형 오픈소스 Android 배포판으로, 지금까지는 사용자가 직접 설치해야 했고 제조사의 공식 사전설치 지원은 없었다. Motorola는 최근 Signature 시리즈 같은 프리미엄 라인업을 통해 고급 스마트폰 시장을 공략해왔으며, 이번 파트너십은 GrapheneOS가 처음으로 대형 제조사와 공식 협력해 하드웨어 단계부터 보안 요건을 충족시키는 사례가 된다.

**「영향」** 이번 파트너십이 실현되면 GrapheneOS는 전문 사용자층을 넘어 사전설치 방식으로 일반 소비자 시장에 진입할 첫 발판을 마련하게 되지만, 은행 앱 등 특정 앱들이 GrapheneOS 환경에서 정상 작동하지 않는 호환성 문제가 여전히 실질적 채택 장벽으로 남아 있다.

**「커뮤니티 반응」** 댓글 참여자들은 사전설치 기기가 Motorola에서 직접 판매되기보다는 제3의 업체를 통해 공급될 가능성이 크다는 점과, 기존 Pixel처럼 사용자 자가 설치 방식도 계속 유지될 것이라는 점을 명확히 했다. 다만 다수는 주요 은행 앱들이 GrapheneOS에서 차단되는 문제를 지적하며, Google 패키지를 우회 설치해도 향후 지속적인 작동을 보장할 수 없다는 실용적 우려를 제기했다.

**태그**: `#open-source`, `#mobile-security`, `#privacy`, `#android`, `#hardware`

---

<a id="item-tech-news-11"></a>
### [Qualcomm, AI 강화한 신형 스마트폰 칩 두 종 출시](https://techcrunch.com/2026/09/22/qualcomm-launches-two-new-smartphone-chips-with-emphasis-on-ai/) ⭐️ 6.0/10

Qualcomm이 AI 성능을 강조한 새로운 스마트폰용 칩 두 종을 발표했다. 이 중 최상위 모델은 300억 개 파라미터 규모의 mixture-of-experts\(MoE\) 모델을 기기 내에서 직접 실행할 수 있다고 밝혔다. 이는 클라우드 서버로 데이터를 전송하지 않고도 스마트폰 자체에서 대형 언어 모델 추론을 처리할 수 있는 능력을 보여주는 것이다. 다만 소스에는 구체적인 칩 이름, 성능 수치, 벤치마크 결과 등 세부 기술 정보는 포함되어 있지 않다.

rss · TechCrunch AI · 9월 22일 20:00

**「배경」** Mixture-of-experts\(MoE\) 모델은 전체 파라미터 규모는 크지만, 특정 작업 처리 시 일부 전문가\(expert\) 서브네트워크만 활성화해 연산량을 줄이는 구조로, 대형 모델을 상대적으로 적은 자원으로 구동할 수 있게 해준다. 이번에 공개된 칩은 2026년형 Qualcomm 플래그십 라인업인 Snapdragon 8 Elite Gen 6와 상위 등급인 Elite Extreme Gen 6로, Extreme 버전은 새로운 Hexagon NPU와 50% 확장된 공유 메모리를 탑재해 최대 30B 파라미터 규모의 MoE 모델을 온디바이스로 구동하는 데 초점을 맞췄다.

**「영향」** 이번 Snapdragon 8 Elite Gen 6 계열 칩은 MoE 구조를 활용해 30B 파라미터급 모델을 온디바이스로 구동함으로써, 스마트폰 제조사와 앱 개발자가 클라우드 의존도를 줄이고 지연 시간과 프라이버시 이점을 갖춘 에이전틱 AI 기능을 탑재한 플래그십 기기를 설계할 수 있게 한다. 다만 Oryon CPU·Adreno GPU·Hexagon NPU·Sensing Hub 간 워크로드 분배와 클라우드 오프로드 경로가 병행되는 구조여서, 실제 성능과 배터리 영향은 기기 출시 후 검증이 필요하다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/22/qualcomm-launches-two-new-smartphone-chips-with-emphasis-on-ai/">Qualcomm launches two new smartphone chips with emphasis on AI | TechCrunch</a></li>
<li><a href="https://www.xda-developers.com/qualcomms-new-snapdragon-8-elite-gen-6-chip-lineup-powerful-ultra-premium-tier/">Qualcomm just split its 2026 flagship Snapdragon 8 Elite Gen 6 chip into two tiers, and the Extreme version features 50% larger shared memory</a></li>
<li><a href="https://www.androidauthority.com/snapdragon-qualcomm-snapdragon-8-elite-gen-6-npu-3709726/">Qualcomm&#x27;s next Snapdragon flagship chip wants your AI agents to stay on-device - Android Authority</a></li>
<li><a href="https://www.androidauthority.com/snapdragon-qualcomm-snapdragon-8-elite-gen-6-npu-3709726/">Qualcomm&#x27;s next Snapdragon flagship chip wants your AI agents to stay on-device - Android Authority</a></li>
<li><a href="https://finance.biggo.com/news/f432da9c-7360-46ba-8c56-1e70ecfb281a">Qualcomm&#x27;s Snapdragon 8 Elite Gen 6 Leak Reveals 5GHz CPU, 30B MoE Support for Agentic AI — BigGo Finance</a></li>

</ul>
</details>

**태그**: `#ai-hardware`, `#smartphone-chips`, `#on-device-ai`, `#qualcomm`, `#model-inference`

---

<a id="item-tech-news-12"></a>
### [Meta, AI 어시스턴트 Muse가 OpenClaw를 모방했다고 인정](https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/) ⭐️ 6.0/10

Meta는 자사 AI 어시스턴트 Muse가 처음부터 새로 개발되었다고 주장해왔지만, 실제로는 OpenClaw에서 '많은 영감을 받았다'는 점을 인정했다. 그 유사성은 단순한 컨셉 수준을 넘어 워크스페이스 파일명과 내부 콘텐츠 구조에까지 나타나는 것으로 확인됐다. 이번 인정은 Meta가 자체 개발을 강조해온 기존 입장과 배치되며, AI 어시스턴트 설계 과정에서 경쟁사 제품의 영향이 어느 정도까지 반영됐는지에 대한 의문을 낳고 있다. 구체적으로 어떤 파일이나 코드가 유사한지, 유사성의 범위와 정도에 대한 세부 내용은 아직 명확히 공개되지 않았다.

rss · TechCrunch AI · 9월 22일 19:09

**「배경」** OpenClaw는 오픈소스로 공개된 AI 어시스턴트 프로젝트로, 워크스페이스 구조나 SOUL.md와 같은 설정 파일 형식 등 독자적인 설계 방식을 갖고 있다. Meta가 자체 제작했다고 밝힌 Muse 어시스턴트에서 이러한 파일명과 내용이 유사하게 발견되면서 사용자들이 문제를 제기했고, 이에 Meta의 Nat Friedman이 OpenClaw의 영향을 인정한 것이다.

**「영향」** 이번 인정은 Meta의 AI 개발 투명성과 독자적 설계 역량에 대한 신뢰도에 의문을 제기하며, 경쟁사 기술을 참고하는 업계 관행에 대한 논의를 촉발할 수 있다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.aichatdaily.com/ai-business/meta-concedes-muse-assistant-heavily-inspired-openclaw">Meta concedes its Muse assistant was heavily inspired by OpenClaw — AI Chat Daily</a></li>

</ul>
</details>

**태그**: `#ai-assistants`, `#meta`, `#design-practices`, `#ai-development`, `#transparency`

---

<a id="item-tech-news-13"></a>
### [Anthropic·OpenAI 신모델, 성능 조금 향상시키고 가격은 대폭 인하](https://arstechnica.com/ai/2026/09/new-anthropic-openai-models-make-same-promise-a-little-more-for-a-lot-less-money/) ⭐️ 6.0/10

Anthropic과 OpenAI가 새로운 모델을 잇달아 출시하면서 공통적으로 이전 대비 소폭 향상된 성능을 훨씬 낮은 가격에 제공한다는 전략을 내세우고 있다. 이는 프론티어 AI 모델 경쟁이 순수 성능 우위 경쟁에서 가격 대비 효율을 따지는 비교 구매 단계로 넘어갔음을 보여준다. 기사 원문은 구체적인 모델명, 버전, 가격표, 벤치마크 수치를 상세히 제공하지 않아 정확한 수치 비교는 제한적이다.

rss · Ars Technica AI · 9월 22일 21:25

**「배경」** Anthropic과 OpenAI는 그동안 GPT, Claude 시리즈의 새 버전을 출시할 때마다 성능 최고치를 갱신하는 데 주력해왔으나, 최근에는 오픈 웨이트 모델을 제공하는 경쟁사들의 압박 속에서 비용 대비 효율을 강조하는 방향으로 전략을 전환하고 있다. 이번 발표는 AI의 잠재적 위협에 대한 우려가 불거진 이후 양사가 내놓은 첫 신규 모델 출시라는 점에서 주목된다.

**「영향」** 개발자와 기업 고객은 이제 모델 선택 시 최고 성능보다 비용 대비 성능을 우선적으로 고려하게 될 가능성이 크며, 이는 API 사용 비용 구조와 제품 설계 전략에 영향을 줄 수 있다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/22/anthropic-openai-cheaper-ai-models.html">Anthropic and OpenAI launch cheaper models</a></li>

</ul>
</details>

**태그**: `#model-updates`, `#pricing`, `#large-language-models`, `#ai-industry`

---

<a id="item-tech-news-14"></a>
### [Microsoft, 12,000개 계정 침해한 AI 공격 플랫폼 'EvilTokens' 차단](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/) ⭐️ 6.0/10

Microsoft는 12,000개 계정을 손상시킨 AI 기반 공격 플랫폼 'EvilTokens'를 차단했다고 밝혔다. 이 플랫폼은 계정 탈취 과정을 자동화하고 가속화하는 엔드-투-엔드 도구를 제공해 대규모 계정 침해를 이전보다 빠르고 쉽게 만든 것으로 알려졌다. Microsoft는 이번 조치를 통해 해당 플랫폼의 운영을 중단시켰으며, 이는 공격자들이 AI 기술을 악용해 사이버 범죄를 고도화하는 최근 추세를 보여주는 사례로 지목된다. 구체적인 공격 기법, 피해 대상 서비스, 플랫폼 운영 주체 등에 대한 세부 정보는 아직 제한적으로 공개된 상태다.

rss · Ars Technica AI · 9월 22일 19:45

**「배경」** EvilTokens는 피싱 서비스\(PhaaS, Phishing-as-a-Service\) 형태로 운영된 도구로, 공격자가 별도의 기술 없이도 대규모 계정 탈취를 자동화할 수 있게 해주는 종합 플랫폼이다. 이 서비스는 2026년 2월 Telegram 채널을 통해 처음 소개되었으며, 초기 가입비 1,500달러와 매월 500달러의 이용료를 부과하는 구독형 모델로 판매되었다. Microsoft의 디지털범죄수사팀\(Digital Crimes Unit, DCU\)이 주도한 이번 대응으로 EvilTokens와 연관된 사이트 50개와 도메인 150개가 압수되었다.

**「영향」** 이번 조치로 10,000개 이상 조직에서 12,000개 이상의 받은편지함을 노린 device code 피싱 기반 BEC 캠페인이 중단되었으며, 텔레그램을 통해 월 구독료를 받고 툴킷을 판매하던 PhaaS\(Phishing-as-a-Service\) 사업 모델 자체가 타격을 입었다. 다만 유사한 AI 지원 피싱 서비스가 다른 형태로 재등장할 가능성이 있어 기업들은 device code 인증 흐름에 대한 모니터링과 방어를 강화해야 한다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/eviltokens-phaas-disrupted-after-compromising-12-000-microsoft-accounts/">EvilTokens PhaaS disrupted after compromising 12 , 000 Microsoft ...</a></li>
<li><a href="https://cd2.ai/microsoft-disrupts-ai-assisted-platform-that-compromised-12000-accounts/">Microsoft disrupts AI -assisted platform that compromised 12 , 000 ...</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/">Unmasking EvilTokens : Getting to the root of... | Microsoft Security Blog</a></li>
<li><a href="https://theoutpost.ai/news-story/microsoft-and-partners-dismantle-evil-tokens-an-ai-powered-phishing-network-that-stole-1-1-m-31163/">Microsoft Disrupts EvilTokens AI -Powered Phishing Kit</a></li>
<li><a href="https://www.darkreading.com/identity-access-management-security/microsoft-disrupts-eviltokens-device-code-phishing-service">Microsoft Disrupts EvilTokens Device Code Phishing Service</a></li>

</ul>
</details>

**태그**: `#security`, `#ai-misuse`, `#account-compromise`, `#threat-intelligence`

---

<a id="item-tech-news-15"></a>
### [AntLing, UI/UX 디자인 특화 6B 오픈소스 이미지 모델 Ming-Image 공개](https://www.reddit.com/r/LocalLLaMA/comments/1wnipcz/new_6b_image_model_coming_antling_just_open/) ⭐️ 6.0/10

AntLing이 Ming-Image-0.1-Design 계열 모델을 오픈소스로 공개했다. 이 계열에는 Ming-Image-0.1-Design과 Ming-Image-0.1-Design-Layer 두 가지 6B 파라미터 모델이 포함되며, 둘 다 Hugging Face의 inclusionAI 조직 계정을 통해 배포된다. 함께 공개된 Ling UI Design Skill과 Image-to-Editable-PPT Skill이라는 두 가지 에이전트 스킬은 UI 디자인 생성 및 이미지에서 편집 가능한 PPT로의 변환 작업을 지원한다. 공개자는 Ming-Image-0.1-Design이 Artificial Analysis의 UI/UX Design 리더보드에서 오픈웨이트 모델 중 1위를 기록했다고 주장하나, 이는 제출자 측 주장으로 별도의 독립적 검증 내용은 제공되지 않았다.

reddit · r/LocalLLaMA · /u/Sitkin\_Marrel · 9월 22일 19:06

**「배경」** Ming-Image-0.1-Design은 UI, 인포그래픽, 포스터 등 텍스트가 많이 포함된 시각 디자인 생성에 특화된 6B 규모의 text-to-image 모델로, 프롬프트만으로 이미지를 생성하며 텍스트를 이미지 안에 선명하게 렌더링하는 데 중점을 둔다. AntLing\(inclusionAI\)은 Ant Group 산하에서 오픈소스 AI 모델을 개발해온 조직이며, Artificial Analysis는 다양한 AI 모델의 성능을 벤치마크하고 순위를 매기는 독립 평가 플랫폼이다.

**「영향」** UI/UX 디자인용 로컬 배포 이미지 모델을 찾는 개발자와 에이전트 워크플로우 구축자에게 6B 규모의 오픈 가중치 대안이 생겨 저사양 환경에서도 실험이 가능해진다. 다만 tool-2-1에 따르면 1위 리더보드 주장은 자체 저장소 내에 게재된 블라인드 선호도 투표 기반 그래픽으로, 독립적인 제3자 검증은 아직 확인되지 않아 성능 우위를 그대로 받아들이기보다는 별도 검증이 필요하다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://huggingface.co/inclusionAI/Ming-Image-0.1-Design">inclusionAI / Ming - Image - 0 . 1 - Design · Hugging Face</a></li>
<li><a href="https://openrouter.ai/inclusionai/ming-image-0.1-design">Ming Image 0 . 1 Design - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://en.theblockbeats.news/flash/368549">Ant Group Open-Sources 6 B Design Model : Specializing in UI Posters...</a></li>
<li><a href="https://www.orcarouter.ai/blog/hy-image-3-5-vs-ming-image-0-1-design">Hy Image3.5 vs Ming-Image-0.1- Design : Rent or Own Weights</a></li>

</ul>
</details>

**태그**: `#open-source`, `#image-models`, `#model-releases`, `#generative-ai`, `#ui-design`

---

## 심층 분석 · 뉴스레터

<a id="item-tech-blog-1"></a>
### [John Platt가 말하는 Google ERA와 AI 기반 과학 연구](https://www.latent.space/p/john-platt) ⭐️ 7.0/10

rss · Latent Space · 9월 22일 21:07

**「배경」** 많은 과학 문제는 겉보기와 달리 '점수화 가능한 작업\(scoreable task\)'으로 환원될 수 있다는 것이 John Platt 팀의 관찰이다. 즉 문제를 평가할 점수 함수만 정의하면 그 점수를 최대화하는 코드를 찾는 문제로 바꿀 수 있는데, 어려운 부분은 점수 함수를 제대로 설계하는 일이며 그다음 최적화 과정 역시 상당한 노력이 필요했다는 것이 출발점이다.

**「방안」** 이 관찰에서 나온 것이 Google의 Empirical Research Assistance\(ERA\)로, 저자에 따르면 개념적으로는 단순하다. Gemini 같은 LLM이 과거 실험 노트북들의 트리를 관리하고, Monte Carlo Tree Search와 유사한 방식으로 Upper Confidence Bound 규칙을 써서 매번 가장 유망해 보이는 노트북을 골라 변형\(mutation\)을 제안한다. 이는 탐욕적이지 않고 낙관적인 탐색이라 가끔은 다섯 번째로 유망한 노트북도 선택되며, 각 분기의 이력이 공유되어 서로 다른 실험 갈래들이 서로에게서 배울 수 있다. 저자는 이를 '잠들지 않는 열정적인 대학원생'에 비유하면서, 진화 알고리즘 자체는 1970년대부터 있었지만 Gemini가 실제로 어디를 봐야 할지 안다는 점이 핵심이며, Gemini 2.0에서 2.5로 넘어가면서 이 접근이 아예 작동하지 않던 상태에서 잘 작동하는 상태로 급변했다고 밝힌다. ERA는 실제로 비행운\(contrail\) 저감 문제를 비롯해 여러 기후 관련 난제를 풀어 최소 열 편의 논문 성과로 이어졌다고 저자는 설명한다. 다만 저자는 강력한 최적화 도구일수록 과적합과 Goodhart의 법칙 위험이 크다고 경고하며, Google의 contrail 탐지 대회 우승자들이 실제 문제 해결보다 라벨의 픽셀 원점 오차 같은 데이터 특이점을 이용해 점수를 올린 사례를 반례로 든다. 이런 함정을 피하기 위한 그의 조언은 항상 선형회귀나 SVM 같은 단순한 모델부터 시작하라는 것이며, 궁극적으로는 예측 모델이 실제로 기술적으로 타당한지 검증하는 것은 과학자의 몫이라고 강조한다.

**「启示」** 저자의 핵심 메시지는 AI 최적화 도구가 아무리 강력해져도 과학자의 역할이 사라지지 않으며, 오히려 깊은 도메인 전문성과 손으로 직접 문제를 풀어보는 경험이 과적합과 자기기만을 피하는 데 필수적이라는 것이다. 도구가 발전할수록 '너 자신을 속이지 말라'는 Feynman의 원칙이 더 중요해진다는 것이 그의 결론이다.

**태그**: `#generative-ai`, `#scientific-computing`, `#climate-tech`, `#optimization-algorithms`, `#machine-learning-practice`

---

<a id="item-tech-blog-2"></a>
### [Claude Opus 5.5와 GPT-6 Sol/Luna, 가격 전쟁의 새 국면](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 7.0/10

rss · Simon Willison · 9월 22일 23:46

**「배경」** Anthropic의 Claude Opus 5.5와 OpenAI의 GPT-6 Sol, GPT-6 Luna가 거의 동시에 출시되면서, LLM 시장의 가격 경쟁이 다시 한 번 격화됐다. 저자 Simon Willison은 실제 사용과 자신의 pelican SVG 테스트를 통해 이 모델들의 성능과 가격을 직접 비교했다.

**「방안」** 저자에 따르면 GPT-6 Luna는 입력 $0.10/output $0.50\(백만 토큰당\)로, 이전 최애 모델이었던 GPT-5.6 Luna보다도 절반 가격이며 OpenAI 역사상 가장 저렴한 모델 중 하나다. GPT-6 Sol 역시 GPT-5.6 Sol 대비 절반으로 떨어졌고, 이는 11월 예정된 GPT-5.6 가격 인상분까지 감안하면 실질적으로는 더 큰 격차라고 저자는 지적한다. 이에 맞서 Anthropic은 Opus 5.5 가격을 20% 인하해 $4/$20로 조정했고, 특히 캐시 입력 가격은 60% 낮췄는데, 에이전트형 장기 대화에서 입력 토큰의 90% 이상이 캐시로 처리되는 점을 고려하면 이는 실질적 비용 절감 효과가 크다고 저자는 설명한다. 하지만 저자가 직접 실행한 pelican-riding-a-bicycle 테스트에서 Opus 5.5의 'max' 사고 수준은 SVG를 완성하지 못한 채 128,000 토큰 출력 한도에 도달해 응답이 끊겼다. 두 차례 반복해도 같은 결과였고, 각 시도에 약 $2.56과 20분이 소요됐다. 저자는 이를 근거로 'max' 사고 수준이 실질적으로 쓸모없을 수 있다고 우려하며, 반면 Fable 5.1의 max는 오히려 지금까지 본 것 중 최고의 pelican을 그려냈다고 대조한다. 저자는 이제 Codex와 Claude Code에서 GPT-6 Sol과 Opus 5.5를 기본 모델로 사용하고 있으며, Datasette Agent 데모도 GPT-6 Luna로 전환해 SQL 쿼리와 HTML/JavaScript 생성에서 빠르고 유능하다고 평가했다.

**「启示」** 저자는 하위·중위 가격대 모델 시장에서 OpenAI와 Anthropic 간 가격 경쟁이 극심해지고 있음을 보여주는 한편, 가격 인하가 반드시 성능이나 안정성 개선을 동반하지는 않는다는 점—Opus 5.5의 max 모드 실패 사례—을 통해 'thinking' 수준을 높이는 것이 항상 더 나은 결과를 보장하지 않는다는 한계를 함께 지적한다.

**태그**: `#large-language-models`, `#pricing`, `#model-updates`, `#generative-ai`, `#openai`

---