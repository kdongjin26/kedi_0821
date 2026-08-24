# -*- coding: utf-8 -*-
"""중단된 회차(분석8·9·10)의 안내 페이지를 만든다.
분석 내용은 싣지 않고 무엇을 하려 했는지와 왜 멈췄는지만 적는다.
자세한 기록은 각 폴더의 README.md에 있다."""
import io, os, sys
sys.stdout.reconfigure(encoding="utf-8")
OUT = r"C:/Users/DJ/Desktop/KEDI 참여 행동/site/reports"
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--bg:#f6f7f9;--surface:#fff;--ink:#15181c;--muted:#59616a;--line:#dde2e7;
      --accent:#14614a;--soft:#e8f1ec;--warn:#8a5a00;--warnbg:#fdf6e6;--warnline:#e8d9b0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#131619;--surface:#1a1e22;--ink:#e5e9ed;--muted:#98a1aa;--line:#2b3138;
  --accent:#5cc79c;--soft:#152a23;--warn:#e0b562;--warnbg:#241f14;--warnline:#4a3f22}}
:root[data-theme="dark"]{--bg:#131619;--surface:#1a1e22;--ink:#e5e9ed;--muted:#98a1aa;
  --line:#2b3138;--accent:#5cc79c;--soft:#152a23;--warn:#e0b562;--warnbg:#241f14;--warnline:#4a3f22}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);word-break:keep-all;line-height:1.75;
  font-family:"IBM Plex Sans KR","Malgun Gothic",system-ui,-apple-system,sans-serif;}
.wrap{max-width:760px;margin:0 auto;padding:44px 28px 72px}
.badge{display:inline-block;padding:5px 13px;border-radius:999px;font-size:.76rem;
  font-weight:700;letter-spacing:.02em;background:var(--warnbg);color:var(--warn);
  border:1px solid var(--warnline);margin-bottom:18px}
h1{margin:0 0 6px;font-size:1.55rem;font-weight:700;letter-spacing:-.02em;line-height:1.35}
.sub{margin:0 0 30px;color:var(--muted);font-size:.95rem}
h2{margin:34px 0 12px;font-size:1.06rem;font-weight:700;color:var(--accent);
   padding-bottom:7px;border-bottom:1px solid var(--line)}
p{margin:0 0 14px}
ul{margin:0 0 14px;padding-left:20px}
li{margin-bottom:7px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:11px;
  padding:20px 22px;margin:18px 0}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.9rem}
th,td{border:1px solid var(--line);padding:8px 11px;text-align:left}
th{background:var(--soft);font-weight:600}
td.num{text-align:right;font-variant-numeric:tabular-nums}
.note{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);
  color:var(--muted);font-size:.86rem}
code{background:var(--soft);padding:1px 6px;border-radius:4px;font-size:.88em}
"""

PAGES = {
"analysis8": dict(
  title="분석8 — 네 구성개념의 다문항 잠재변수 모형",
  date="2026-08-24 중단",
  goal="""<p>관용의식·참여의식·준법의식·봉사의식 네 가지를 각각 <strong>다문항 잠재변수</strong>로
구성하고, 2차 잠재성장모형(curve-of-factors)으로 성인 초기 정치참여를 예측하려 하였다.
기존 회차의 최대 한계였던 <strong>측정오차 통제</strong>를 해결하는 것이 목적이었다.</p>""",
  why="""<p>문항 18개 × 6시점 = <strong>관측변수 108개</strong>에 순서형 종속변수 3개와 공변인 7개를
붙인 WLSMV 모형이었다. 무조건 모형은 CFI .922~.981로 잘 수렴했으나, 종속변수를 붙이자
적합도가 무너졌다.</p>
<table><tr><th>단독 투입 (10차)</th><th>CFI</th><th>RMSEA</th></tr>
<tr><td>관용의식</td><td class="num">.895</td><td class="num">.034</td></tr>
<tr><td>참여의식</td><td class="num">.884</td><td class="num">.041</td></tr>
<tr><td>준법의식</td><td class="num">.891</td><td class="num">.039</td></tr>
<tr><td>봉사의식</td><td class="num">.884</td><td class="num">.038</td></tr></table>
<p>네 구성 동시 투입은 메모리 3GB를 쓰다가 중단하였다.</p>""",
  kept="""<ul>
<li>차수마다 문항 번호와 하위영역 이름이 바뀐다는 점을 확인하고 <strong>문구 기준 대응표</strong>를 만들었다.</li>
<li>네 구성의 판별타당도가 좋다(요인 간 상관 .370~.638).</li>
<li>관용의식 11문항은 하나로 묶이지 않는다. 다문화 관계 6문항만 쓰는 편이 낫다(CFI .944 대 .872).</li>
<li>네 구성의 변화 방향이 둘씩 갈린다. 관용·준법은 자라고 참여·봉사는 꺾인다.</li>
</ul>"""),

"analysis9": dict(
  title="분석9 — 중3·고3 두 시점의 조건부 예측력 비교",
  date="2026-08-24 중단",
  goal="""<p>성장모형을 쓰지 않고 <strong>두 시점의 조건부 예측력</strong>을 비교하려 하였다.
중학교 3학년과 고등학교 3학년의 참여 관련 태도가 동일한 성인 초기 정치참여를 각각 어느 정도
예측하며, 두 시점이 서로 독립적인 예측력을 갖는지 묻는 설계다.</p>
<table><tr><th>모형</th><th>예측변수</th></tr>
<tr><td>A</td><td>중3(5차) 태도 + 통제변수</td></tr>
<tr><td>B</td><td>고3(8차) 태도 + 통제변수</td></tr>
<tr><td><strong>C</strong></td><td><strong>중3 + 고3 동시 + 통제변수</strong> ← 핵심</td></tr></table>
<p>A와 B를 따로 돌려 계수를 비교하는 것으로는 부족하다. 같은 사람의 같은 종속변수를
예측하므로 두 계수가 서로 연관되어 있기 때문이다.</p>""",
  why="""<p>모형은 돌렸으나 <strong>결과를 확정하지 않았다.</strong> 표·그림·보고서를 만들지 않았고,
참여의식의 조작화(어느 문항을 쓸지)를 최종적으로 정하지 못한 상태에서 멈췄다.</p>
<p>완전제거의 선택 편의가 다른 회차보다 크다는 점(학업성취 d = +0.34)도 해소하지 못했다.
다중대체를 민감도로 검토하려 했으나 하지 않았다.</p>""",
  kept="""<ul>
<li><strong>설계 타당성은 확인되었다.</strong> 두 시점만 요구하므로 6시점 요구보다 표본이 늘어난다
(10차 4,669 / 12차 4,239).</li>
<li><strong>다중공선성이 문제가 되지 않는다.</strong> 중3–고3 상관이 .307~.444로 낮고
(3년 간격), 모형 C의 예측변수 VIF는 1.24~1.65다. 통제변수 최대 VIF(2.04)보다 낮다.</li>
<li>고3 계수를 "중3 이후 변화의 효과"라고 부르면 안 된다. 정확히는
"중3 수준을 통제한 고3 수준의 조건부 연관"이다.</li>
</ul>"""),

"analysis10": dict(
  title="분석10 — 시민적 주체성 2문항 잠재변수",
  date="2026-08-24 중단",
  goal="""<p>참여의식 세 문항 가운데 <strong>행동 지향과 시민 효능감을 하나의 잠재변수</strong>로 묶어
2차 잠재성장모형을 적용하려 하였다. 두 문항은 변화 방향이 같고(−.026, −.012), 세 쌍 중
상관이 가장 높으며(.394~.509), 개념적으로도 "내가 나서면 바뀐다"는 믿음과 "문제가 생기면
나선다"는 성향으로 묶인다.</p>""",
  why="""<p>2차 잠재성장모형이 <strong>부적절 해</strong>를 냈다. 잔차분산이 음수인 관측변수가
나오고 표준화 적재량이 1을 넘었다.</p>
<table><tr><th>사양</th><th>CFI</th><th>음수 분산</th><th>표준화 적재량 (행동/효능)</th></tr>
<tr><td>잔차상관 전체</td><td class="num">.990</td><td class="num">2개</td><td class="num">1.081 / .477</td></tr>
<tr><td>행동 지향만</td><td class="num">.983</td><td class="num">0개</td><td class="num">.613 / .818</td></tr>
<tr><td>잔차상관 없음</td><td class="num">.816</td><td class="num">0개</td><td class="num">.892 / .569</td></tr></table>
<p>요인이 사실상 행동 지향 그 자체가 되었고, 부적절 해를 피하는 사양에서는
<strong>적재량이 역전된다.</strong> 사양을 조금 바꾸면 요인의 정체가 뒤바뀌므로 안정적이지 않다.</p>
<p>두 문항의 상관이 중1 .509에서 고3 .394로 떨어지는 것이 원인이다. 공통분이 시간이 갈수록
줄어드는데 2문항이라 그 흔들림을 흡수할 여지가 없다.</p>""",
  kept="""<ul>
<li><strong>종단 측정불변성은 완벽하게 성립했다</strong>(스칼라 ΔCFI = −.002).
3문항 사양의 −.011과 대조된다. 인지적 관여를 빼면 불변성 문제가 사라진다는 예상은 맞았다.</li>
<li>인지적 관여가 나머지 둘과 다른 것을 잰다는 점이 또 한 번 확인되었다.</li>
</ul>"""),
}

TPL = """<title>{title}</title>
<style>{css}</style>
<div class="wrap">
  <span class="badge">미완성 · {date}</span>
  <h1>{title}</h1>
  <p class="sub">이 회차는 완성되지 않았다. 아래는 무엇을 하려 했고 왜 멈췄는지에 대한 기록이다.</p>

  <h2>무엇을 하려 했나</h2>
  {goal}

  <h2>왜 멈췄나</h2>
  {why}

  <h2>그럼에도 확인된 것</h2>
  {kept}

  <div class="note">
    자세한 기록·수치·재현 스크립트는 프로젝트 폴더의 <code>README.md</code>에 있다.
    이 회차의 결과는 확정된 것이 아니므로 인용하지 않는다.
  </div>
</div>
"""

for name, d in PAGES.items():
    html = TPL.format(css=CSS, **d)
    io.open(f"{OUT}/{name}.html", "w", encoding="utf-8").write(html)
    print(f"SAVED reports/{name}.html  ({len(html):,} bytes)")
