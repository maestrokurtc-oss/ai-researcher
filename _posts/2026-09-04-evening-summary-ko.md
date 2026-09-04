---
layout: default
title: "AI 브리핑 · 2026-09-04 저녁"
date: 2026-09-04
lang: ko
---

> 수집한 67건 중 1건을 골랐습니다.

---

**업계 동향**
1. [ID 검증 업체, 1년 넘게 해커에게 스캔 정보 실시간 노출](#item-tech-news-1) ⭐️ 7.0/10

---

## 업계 동향

<a id="item-tech-news-1"></a>
### [ID 검증 업체, 1년 넘게 해커에게 스캔 정보 실시간 노출](http://www.techdirt.com/2026/09/03/hackers-had-a-live-feed-of-every-id-this-verification-company-scanned-for-over-a-year/) ⭐️ 7.0/10

한 신원 확인\(ID verification\) 업체가 스캔한 신분증 정보에 해커가 1년 이상 실시간으로 접근할 수 있었던 사건이 드러났다. 구체적인 회사명이나 침해 방식에 대한 원문 세부 내용은 확인되지 않았지만, 이 사건은 신원 인증 시스템이 업계 전반에서 어떻게 설계되고 운영되는지에 대한 근본적인 결함을 드러낸 것으로 알려졌다. 커뮤니티에서는 이와 관련해 Brian Krebs가 FBI가 신원 정보를 판매하는 서비스를 조사 중이라는 별도의 기사를 다룬 것으로 언급되었으나, 두 사건의 직접적인 연관성이나 세부 사실은 이 자료만으로는 명확히 확인되지 않는다.

hackernews · beardyw · 9월 4일 06:47 · [커뮤니티 반응](https://news.ycombinator.com/item?id=49561320)

**「배경」** 온라인 서비스에서 사용자의 신원을 확인하기 위해 운전면허증이나 신분증을 스캔해 제출받는 ID 검증\(ID verification\) 회사들이 존재하며, 이 데이터는 은행, 플랫폼 등 다양한 제3자 서비스가 위탁 처리한다. 이번 사건에서는 루이지애나에 기반을 둔 대형 ID 검증 회사의 시스템이 해킹당해 하루 약 50만 건씩 신규 문서가 유출되었고, 러시아 사이버범죄 포럼에서 'Nexus'라는 이름으로 판매되었으며 미 국방장관 Pete Hegseth의 면허증도 포함된 것으로 알려졌다. 유출 규모는 미국과 캐나다의 약 1억 5,300만 건에 달하는 신분증 스캔본으로 추정된다.

**「영향」** 이번 유출로 신원 검증에 의존하는 렌터카 업체, 대마초 판매점 등 idscan.net 시스템 이용 업체들의 고객 개인정보가 대량 노출되었으며, Krebs on Security 보도에 따르면 1억 5300만 건 이상의 운전면허증 정보가 판매 서비스에서 유통된 것으로 확인되었다. FBI 뉴올리언스 지부가 이미 조사에 착수한 상태로, PKI 기반 인증서 발급이나 정부 주도 디지털 신원증명\(예: 아일랜드 정부 디지털 월렛\) 같은 대안 설계로의 전환 압력이 업계 전반에 커질 것으로 보인다.

**「커뮤니티 반응」** 일부 개발자는 현재의 ID 검증 방식이 처음부터 구조적으로 취약하다고 지적하며, PKI 기반의 신뢰 체인이나 서비스별 개별 인증서, 제로 지식 증명\(zero-knowledge proof\) 도입을 대안으로 제시했다. 다른 참여자들은 정부가 직접 운영하는 디지털 신원 지갑\(예: 아일랜드 정부 디지털 월렛\)이 다수의 민간 제3자 업체에 정보를 맡기는 것보다 낫다는 의견을 냈고, 비기술적 의사결정자들이 보안과 편의성을 동시에 요구하는 비현실적 기대가 문제의 근본 원인이라는 비판도 있었다.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/02/it-sure-looks-like-hackers-breached-a-major-id-card-verification-service/">It sure looks like hackers breached a major ID card verification service</a></li>
<li><a href="https://futurism.com/future-society/hackers-selling-stolen-scans-americans-drivers-licenses">Hackers Are Selling Stolen Scans of 153 Million US and Canadian...</a></li>
<li><a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">FBI Probes Service Selling 153M+ Drivers Licenses – Krebs on Security</a></li>
<li><a href="https://daily.dev/posts/fbi-probes-service-selling-153m-drivers-licenses-krebs-on-security-bmalidm3f">FBI Probes Service Selling 153M+ Drivers Licenses – Krebs on Security | daily.dev</a></li>

</ul>
</details>

**태그**: `#security-breach`, `#identity-verification`, `#infrastructure-vulnerability`, `#authentication-systems`, `#privacy`

---