---
layout: default
title: Home
---

# AI 리서처 브리핑

AI 관련 뉴스·논문·업계 동향을 자동으로 모아 **하루 두 번**(오전 9시 / 저녁 7시, 한국 시간) 한국어로 정리합니다.

수집원은 arXiv, Hacker News, Reddit, AI 랩 공식 블로그, 업계 뉴스, 뉴스레터, GitHub 릴리스입니다. 수집한 항목을 AI가 중요도 0–10으로 채점하고, 기준을 넘은 것만 요약해 싣습니다.

소스와 파이프라인은 [GitHub 저장소](https://github.com/maestrokurtc-oss/ai-researcher)에 있습니다. [Thysrael/Horizon](https://github.com/Thysrael/Horizon)을 포크해 만들었습니다.

## 브리핑 <a class="rss-icon" href="{{ '/feed-ko.xml' | relative_url }}" aria-label="RSS 구독"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a>

<ul>
  {% assign ko_posts = site.posts | where: "lang", "ko" %}
  {% for post in ko_posts limit:60 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% else %}
    <li><em>아직 브리핑이 없습니다.</em></li>
  {% endfor %}
</ul>

## 문서

- [설정 가이드](configuration) — AI 제공자, 정보원, 필터링, 환경변수 치환
- [소스 수집기](scrapers) — GitHub·Hacker News·RSS·Reddit 수집 방식
- [프로필](profiles) — 항목 성격별 채점 기준과 요약 형식
