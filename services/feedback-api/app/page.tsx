export default function Home() {
  return (
    <main className="status-page">
      <section className="status-card" aria-labelledby="service-title">
        <div className="status-mark" aria-hidden="true">✓</div>
        <p className="eyebrow">AI RESEARCHER</p>
        <h1 id="service-title">피드백 저장소가 작동 중입니다</h1>
        <p className="lede">
          브리핑의 좋아요·별로예요 선택을 개인을 직접 식별하지 않는 이벤트로 보관합니다.
        </p>
        <dl className="service-facts">
          <div>
            <dt>수집 정보</dt>
            <dd>콘텐츠 반응과 AI 점수</dd>
          </div>
          <div>
            <dt>보관하지 않음</dt>
            <dd>이름, 이메일, 원본 브라우저 ID·IP</dd>
          </div>
          <div>
            <dt>사용 목적</dt>
            <dd>향후 선별 품질 분석과 개선</dd>
          </div>
        </dl>
        <p className="privacy-detail">
          원본 식별값은 중복·남용 완화를 위해 서버에서 즉시 일방향 변환하며,
          IP 기반 제한 정보는 2시간 뒤 만료되고 후속 요청 때 삭제됩니다.
        </p>
        <a className="back-link" href="https://maestrokurtc-oss.github.io/ai-researcher/">
          AI 리서처 브리핑으로 돌아가기 <span aria-hidden="true">→</span>
        </a>
      </section>
    </main>
  );
}
