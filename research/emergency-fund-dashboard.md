---
Parent: "[[AREA - Фінанси]]"
tags:
  - фінанси
  - emergency-fund
  - dashboard
last_updated: 2026-06-25
monthly_expenses: 2000
target_total: 18000
target_phase_1: 6000
target_phase_2: 12000
target_phase_3: 18000
cash_home: 800
card_usd: 1400
usdt_cex: 0
ovdp_short: 1111.57
ucits_short: 845
usdt_earn_short: 0
ovdp_long: 0
ucits_long: 0
usdt_earn_long: 0
---

> 💡 **Як користуватись:** редагуй значення у Properties (Ctrl+;) — суми по інструментах. Дашборд оновиться автоматично. Цільові суми (target_*) і місячні витрати теж тут.

```dataviewjs
const f = dv.current();

// === ДАНІ ===
const instruments = [
  { id: 'cash_home',       name: 'Готівка USD вдома',        level: 1, target: 1000, color: '#10b981', category: 'cash',   geo: 'out', icon: '💵' },
  { id: 'card_usd',        name: 'USD на картковому рахунку', level: 1, target: 1400, color: '#10b981', category: 'cash',   geo: 'in',  icon: '💳' },
  { id: 'usdt_cex',        name: 'USDT WhiteBIT (instant)',    level: 1, target: 600,  color: '#10b981', category: 'crypto', geo: 'out', icon: '⚡' },
  { id: 'ovdp_short',      name: 'USD ОВДП (mono банка)',      level: 2, target: 2400, color: '#f59e0b', category: 'bonds',  geo: 'in',  icon: '🇺🇦' },
  { id: 'ucits_short',     name: 'iShares USD 0-1yr Acc IE00BGSF1X88 (Freedom24)', level: 2, target: 2400, color: '#f59e0b', category: 'bonds',  geo: 'out', icon: '🇺🇸' },
  { id: 'usdt_earn_short', name: 'USDT Earn lock 30 дн (WhiteBIT/Binance)', level: 2, target: 1200, color: '#f59e0b', category: 'crypto', geo: 'out', icon: '🟡' },
  { id: 'ovdp_long',       name: 'USD ОВДП (mono банка)',      level: 3, target: 2600, color: '#3b82f6', category: 'bonds',  geo: 'in',  icon: '🇺🇦' },
  { id: 'ucits_long',      name: 'iShares USD 0-1yr + 1-3yr Acc (Freedom24)',      level: 3, target: 4400, color: '#3b82f6', category: 'bonds',  geo: 'out', icon: '🇺🇸' },
  { id: 'usdt_earn_long',  name: 'USDT+USDC Earn 90 дн (WhiteBIT/Binance)', level: 3, target: 2000, color: '#3b82f6', category: 'crypto', geo: 'out', icon: '🔵' }
];

const monthlyExpenses = Number(f.monthly_expenses) || 2000;
const targetTotal = Number(f.target_total) || 18000;
const phaseTargets = {
  1: Number(f.target_phase_1) || 6000,
  2: Number(f.target_phase_2) || 12000,
  3: Number(f.target_phase_3) || 18000
};

instruments.forEach(i => i.current = Number(f[i.id]) || 0);

const totalCurrent = instruments.reduce((s, i) => s + i.current, 0);
const totalTarget  = instruments.reduce((s, i) => s + i.target, 0);
const overallPct   = totalTarget ? (totalCurrent / totalTarget * 100) : 0;
const monthsCovered = totalCurrent / monthlyExpenses;

const fmt$ = n => '$' + Math.round(n).toLocaleString('en-US');
const fmtPct = n => n.toFixed(1) + '%';

// === HEAD ===
dv.el('h1', '🛡️ Emergency Fund Dashboard', { attr: { style: 'margin: 0 0 0.5rem 0;' }});
dv.el('div', `Оновлено: ${f.last_updated || 'не вказано'} · Мін. витрати: ${fmt$(monthlyExpenses)}/міс`, {
  attr: { style: 'color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem;' }
});

// === HERO BLOCK ===
const heroPct = Math.min(overallPct, 100);
const heroColor = overallPct < 33 ? '#ef4444' : overallPct < 66 ? '#f59e0b' : overallPct < 100 ? '#3b82f6' : '#10b981';

const heroHTML = `
<div style="background: linear-gradient(135deg, var(--background-modifier-card) 0%, rgba(0,0,0,0.15) 100%); border: 2px solid ${heroColor}; border-radius: 16px; padding: 1.8rem; margin-bottom: 2rem; box-shadow: 0 8px 24px rgba(0,0,0,0.25);">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
    <div>
      <div style="color: #94a3b8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;">Загалом накопичено</div>
      <div style="color: var(--text-normal); font-size: 3rem; font-weight: 900; line-height: 1;">${fmt$(totalCurrent)}</div>
      <div style="color: #94a3b8; font-size: 0.95rem; margin-top: 0.3rem;">з ${fmt$(targetTotal)} (${fmtPct(overallPct)})</div>
    </div>
    <div style="text-align: right;">
      <div style="color: #94a3b8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;">Покриття витрат</div>
      <div style="color: ${heroColor}; font-size: 3rem; font-weight: 900; line-height: 1;">${monthsCovered.toFixed(1)} <span style="font-size: 1.2rem; color: #94a3b8;">міс</span></div>
      <div style="color: #94a3b8; font-size: 0.95rem; margin-top: 0.3rem;">ціль: 9 міс</div>
    </div>
  </div>
  <div style="margin-top: 1.5rem; background: rgba(148, 163, 184, 0.15); border-radius: 8px; height: 14px; overflow: hidden;">
    <div style="background: linear-gradient(90deg, ${heroColor} 0%, ${heroColor}dd 100%); height: 100%; width: ${heroPct}%; transition: width 0.6s; box-shadow: 0 0 12px ${heroColor}88;"></div>
  </div>
</div>`;
dv.el('div', heroHTML);

// === ФАЗИ ===
dv.el('h2', '🎯 Прогрес по фазах', { attr: { style: 'margin: 1.5rem 0 0.8rem 0;' }});

const phases = [
  { num: 1, name: 'Мінімум',  months: 3, target: phaseTargets[1], color: '#ef4444' },
  { num: 2, name: 'Базова',   months: 6, target: phaseTargets[2], color: '#f59e0b' },
  { num: 3, name: 'Повна',    months: 9, target: phaseTargets[3], color: '#10b981' }
];

const phaseCards = phases.map(p => {
  const pct = Math.min(totalCurrent / p.target * 100, 100);
  const done = totalCurrent >= p.target;
  return `
<div style="flex: 1; min-width: 180px; background: var(--background-modifier-card); border: 2px solid ${done ? '#10b981' : p.color}; border-radius: 12px; padding: 1rem;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
    <div style="color: ${done ? '#10b981' : p.color}; font-weight: 700; font-size: 0.95rem;">${done ? '✅' : '⏳'} Фаза ${p.num} · ${p.name}</div>
    <div style="color: #94a3b8; font-size: 0.75rem;">${p.months} міс</div>
  </div>
  <div style="color: var(--text-normal); font-size: 1.5rem; font-weight: 800;">${fmt$(Math.min(totalCurrent, p.target))} <span style="color: #64748b; font-size: 0.9rem; font-weight: 500;">/ ${fmt$(p.target)}</span></div>
  <div style="background: rgba(148, 163, 184, 0.15); border-radius: 6px; height: 8px; margin-top: 0.6rem; overflow: hidden;">
    <div style="background: ${done ? '#10b981' : p.color}; height: 100%; width: ${pct}%;"></div>
  </div>
  <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 0.4rem; text-align: right;">${fmtPct(pct)}</div>
</div>`;
}).join('');

dv.el('div', `<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem;">${phaseCards}</div>`);

// === РІВНІ ===
dv.el('h2', '🪜 Рівні доступу', { attr: { style: 'margin: 1.5rem 0 0.8rem 0;' }});

const levels = [
  { num: 1, name: 'Критичний',     access: 'години',     color: '#10b981' },
  { num: 2, name: 'Буфер 2–3 міс', access: '1–3 дні',    color: '#f59e0b' },
  { num: 3, name: 'Стратегічний',  access: '1–2 тижні',  color: '#3b82f6' }
];

const levelCards = levels.map(l => {
  const items = instruments.filter(i => i.level === l.num);
  const cur = items.reduce((s, i) => s + i.current, 0);
  const tgt = items.reduce((s, i) => s + i.target, 0);
  const pct = tgt ? Math.min(cur / tgt * 100, 100) : 0;
  return `
<div style="background: var(--background-modifier-card); border-left: 4px solid ${l.color}; border-radius: 8px; padding: 1.2rem; margin-bottom: 1rem;">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.8rem;">
    <div>
      <div style="color: ${l.color}; font-weight: 700; font-size: 1.05rem;">Рівень ${l.num} · ${l.name}</div>
      <div style="color: #94a3b8; font-size: 0.8rem;">доступ: ${l.access}</div>
    </div>
    <div style="text-align: right;">
      <div style="color: var(--text-normal); font-size: 1.4rem; font-weight: 700;">${fmt$(cur)} <span style="color: #64748b; font-size: 0.85rem; font-weight: 500;">/ ${fmt$(tgt)}</span></div>
      <div style="color: ${l.color}; font-size: 0.85rem;">${fmtPct(pct)}</div>
    </div>
  </div>
  <div style="background: rgba(148, 163, 184, 0.15); border-radius: 4px; height: 6px; overflow: hidden; margin-bottom: 0.8rem;">
    <div style="background: ${l.color}; height: 100%; width: ${pct}%;"></div>
  </div>
  <div style="display: flex; flex-direction: column; gap: 0.3rem;">
    ${items.map(i => {
      const ipct = i.target ? Math.min(i.current / i.target * 100, 100) : 0;
      const gap = i.target - i.current;
      return `
    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; padding: 0.3rem 0; border-bottom: 1px dashed rgba(148,163,184,0.15);">
      <span style="color: var(--text-normal);">${i.icon} ${i.name}</span>
      <span style="color: ${i.current >= i.target ? '#10b981' : '#94a3b8'};">${fmt$(i.current)} / ${fmt$(i.target)} ${gap > 0 ? `<span style='color:#ef4444; font-size: 0.75rem;'>(−${fmt$(gap)})</span>` : '<span style=\"color:#10b981;\">✓</span>'}</span>
    </div>`;
    }).join('')}
  </div>
</div>`;
}).join('');

dv.el('div', levelCards);

// === ЧАРТИ ===
dv.el('h2', '📊 Структура портфеля', { attr: { style: 'margin: 2rem 0 1rem 0;' }});

const catLabels = { cash: 'Готівка / Картка', bonds: 'Облігації', crypto: 'Крипто-стейбли' };
const catColors = { cash: '#10b981', bonds: '#3b82f6', crypto: '#f59e0b' };
const byCat = ['cash', 'bonds', 'crypto'].map(c => ({
  cat: c,
  current: instruments.filter(i => i.category === c).reduce((s, i) => s + i.current, 0),
  target:  instruments.filter(i => i.category === c).reduce((s, i) => s + i.target, 0)
}));

// --- Donut: за категоріями (центрований, фіксована висота) ---
const donutBox = dv.el('div', '', { attr: { style: 'background: var(--background-modifier-card); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem;' }});
donutBox.createEl('div', { text: '🥧 За типом активу', attr: { style: 'color: var(--text-normal); font-weight: 600; font-size: 1.05rem; margin-bottom: 1rem; text-align: center;' }});

const donutWrap = donutBox.createEl('div', { attr: { style: 'max-width: 420px; height: 280px; margin: 0 auto;' }});

if (totalCurrent > 0) {
  window.renderChart({
    type: 'doughnut',
    data: {
      labels: byCat.map(c => catLabels[c.cat]),
      datasets: [{
        data: byCat.map(c => c.current),
        backgroundColor: byCat.map(c => catColors[c.cat]),
        borderColor: 'var(--background-primary)',
        borderWidth: 3,
        hoverOffset: 10
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { color: '#e2e8f0', padding: 12, font: { size: 12 }, usePointStyle: true }
        },
        tooltip: {
          callbacks: {
            label: (ctx) => {
              const val = ctx.parsed;
              const sum = ctx.dataset.data.reduce((a, b) => a + b, 0);
              const p = sum ? (val / sum * 100).toFixed(1) : 0;
              return ` ${ctx.label}: $${val.toLocaleString('en-US')} (${p}%)`;
            }
          }
        }
      }
    }
  }, donutWrap);
} else {
  donutWrap.createEl('div', { text: 'Поки немає даних — заповни Properties зверху', attr: { style: 'color: #64748b; text-align: center; padding-top: 6rem;' }});
}

// --- Категорії: міні-картки під донатом ---
const catCardsHTML = `
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; margin-bottom: 1.5rem;">
${byCat.map(c => {
  const pct = c.target ? Math.min(c.current / c.target * 100, 100) : 0;
  const sharePct = totalCurrent ? (c.current / totalCurrent * 100) : 0;
  return `
  <div style="background: var(--background-modifier-card); border-left: 3px solid ${catColors[c.cat]}; border-radius: 6px; padding: 0.7rem 0.9rem;">
    <div style="color: ${catColors[c.cat]}; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em;">${catLabels[c.cat]}</div>
    <div style="color: var(--text-normal); font-size: 1.3rem; font-weight: 800; margin-top: 0.2rem;">${fmt$(c.current)}</div>
    <div style="color: #94a3b8; font-size: 0.8rem;">з ${fmt$(c.target)} · ${fmtPct(pct)} цілі</div>
    <div style="color: #cbd5e1; font-size: 0.75rem; margin-top: 0.3rem;">📊 ${fmtPct(sharePct)} портфеля</div>
  </div>`;
}).join('')}
</div>`;
dv.el('div', catCardsHTML);

// --- Bar: current vs target по інструментах (full width, висока) ---
const barBox = dv.el('div', '', { attr: { style: 'background: var(--background-modifier-card); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem;' }});
barBox.createEl('div', { text: '📊 Current vs Target по інструментах', attr: { style: 'color: var(--text-normal); font-weight: 600; font-size: 1.05rem; margin-bottom: 1rem; text-align: center;' }});
const barWrap = barBox.createEl('div', { attr: { style: 'height: 420px; width: 100%;' }});

window.renderChart({
  type: 'bar',
  data: {
    labels: instruments.map(i => `${i.icon} ${i.name}`),
    datasets: [
      { label: 'Current', data: instruments.map(i => i.current), backgroundColor: '#10b981', borderRadius: 4 },
      { label: 'Target',  data: instruments.map(i => i.target),  backgroundColor: 'rgba(148, 163, 184, 0.35)', borderRadius: 4 }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    scales: {
      x: {
        ticks: { color: '#94a3b8', callback: (v) => '$' + v.toLocaleString('en-US') },
        grid: { color: 'rgba(148,163,184,0.1)' }
      },
      y: { ticks: { color: '#cbd5e1', font: { size: 12 }}, grid: { display: false }}
    },
    plugins: {
      legend: { labels: { color: '#e2e8f0', font: { size: 12 }, usePointStyle: true }},
      tooltip: {
        callbacks: {
          label: (ctx) => ` ${ctx.dataset.label}: $${ctx.parsed.x.toLocaleString('en-US')}`
        }
      }
    }
  }
}, barWrap);

// === ГЕОГРАФІЯ ===
const inSum  = instruments.filter(i => i.geo === 'in').reduce((s, i) => s + i.current, 0);
const outSum = instruments.filter(i => i.geo === 'out').reduce((s, i) => s + i.current, 0);
const inTgt  = instruments.filter(i => i.geo === 'in').reduce((s, i) => s + i.target, 0);
const outTgt = instruments.filter(i => i.geo === 'out').reduce((s, i) => s + i.target, 0);
const inPct  = totalCurrent ? (inSum / totalCurrent * 100) : 0;
const outPct = totalCurrent ? (outSum / totalCurrent * 100) : 0;

const geoHTML = `
<h2 style="margin: 1.5rem 0 0.8rem 0;">🌍 Географічний розподіл</h2>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 2rem;">
  <div style="background: var(--background-modifier-card); border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 12px; padding: 1.2rem;">
    <div style="color: #ef4444; font-weight: 700; margin-bottom: 0.4rem;">🇺🇦 Внутрішній</div>
    <div style="color: var(--text-normal); font-size: 1.6rem; font-weight: 800;">${fmt$(inSum)} <span style="color: #64748b; font-size: 0.85rem; font-weight: 500;">/ ${fmt$(inTgt)}</span></div>
    <div style="color: #94a3b8; font-size: 0.85rem;">${fmtPct(inPct)} від поточного · ціль ~36%</div>
  </div>
  <div style="background: var(--background-modifier-card); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 12px; padding: 1.2rem;">
    <div style="color: #10b981; font-weight: 700; margin-bottom: 0.4rem;">🌐 Зовнішній</div>
    <div style="color: var(--text-normal); font-size: 1.6rem; font-weight: 800;">${fmt$(outSum)} <span style="color: #64748b; font-size: 0.85rem; font-weight: 500;">/ ${fmt$(outTgt)}</span></div>
    <div style="color: #94a3b8; font-size: 0.85rem;">${fmtPct(outPct)} від поточного · ціль ~64%</div>
  </div>
</div>`;
dv.el('div', geoHTML);

// === ТАБЛИЦЯ ВСІХ ІНСТРУМЕНТІВ ===
dv.el('h2', '📋 Усі інструменти', { attr: { style: 'margin: 1.5rem 0 0.8rem 0;' }});

const tableHTML = `
<table style="width: 100%; border-collapse: collapse; background: var(--background-modifier-card); border-radius: 8px; overflow: hidden;">
  <thead>
    <tr style="background: rgba(148, 163, 184, 0.1);">
      <th style="padding: 0.7rem; text-align: left; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">Інструмент</th>
      <th style="padding: 0.7rem; text-align: center; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">Рівень</th>
      <th style="padding: 0.7rem; text-align: right; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">Current</th>
      <th style="padding: 0.7rem; text-align: right; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">Target</th>
      <th style="padding: 0.7rem; text-align: right; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">Gap</th>
      <th style="padding: 0.7rem; text-align: right; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">%</th>
    </tr>
  </thead>
  <tbody>
    ${instruments.map(i => {
      const gap = i.target - i.current;
      const pct = i.target ? (i.current / i.target * 100) : 0;
      const pctColor = pct >= 100 ? '#10b981' : pct >= 50 ? '#f59e0b' : '#ef4444';
      return `
    <tr style="border-bottom: 1px solid rgba(148, 163, 184, 0.1);">
      <td style="padding: 0.7rem; color: var(--text-normal);">${i.icon} ${i.name}</td>
      <td style="padding: 0.7rem; text-align: center; color: ${i.color}; font-weight: 600;">Р${i.level}</td>
      <td style="padding: 0.7rem; text-align: right; color: var(--text-normal); font-weight: 600;">${fmt$(i.current)}</td>
      <td style="padding: 0.7rem; text-align: right; color: #94a3b8;">${fmt$(i.target)}</td>
      <td style="padding: 0.7rem; text-align: right; color: ${gap > 0 ? '#ef4444' : '#10b981'};">${gap > 0 ? '−' + fmt$(gap) : '✓'}</td>
      <td style="padding: 0.7rem; text-align: right; color: ${pctColor}; font-weight: 600;">${fmtPct(pct)}</td>
    </tr>`;
    }).join('')}
    <tr style="background: rgba(148, 163, 184, 0.08); font-weight: 700;">
      <td style="padding: 0.8rem; color: var(--text-normal);">∑ Усього</td>
      <td></td>
      <td style="padding: 0.8rem; text-align: right; color: var(--text-normal);">${fmt$(totalCurrent)}</td>
      <td style="padding: 0.8rem; text-align: right; color: var(--text-normal);">${fmt$(totalTarget)}</td>
      <td style="padding: 0.8rem; text-align: right; color: #ef4444;">${totalTarget - totalCurrent > 0 ? '−' + fmt$(totalTarget - totalCurrent) : '✓'}</td>
      <td style="padding: 0.8rem; text-align: right; color: ${heroColor};">${fmtPct(overallPct)}</td>
    </tr>
  </tbody>
</table>`;
dv.el('div', tableHTML);

// === ПОТОЧНИЙ ФОКУС ===
const nextLevel = instruments.find(i => i.current < i.target);
let focusHTML;
if (!nextLevel) {
  focusHTML = `
<div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(16, 185, 129, 0.05)); border: 2px solid #10b981; border-radius: 12px; padding: 1.5rem; margin-top: 1.5rem; text-align: center;">
  <div style="color: #10b981; font-size: 1.5rem; font-weight: 800;">🎉 Фонд повністю сформований</div>
  <div style="color: #94a3b8; margin-top: 0.4rem;">Перейти на квартальний ребаланс. DCA $500/міс у портфель.</div>
</div>`;
} else {
  const gap = nextLevel.target - nextLevel.current;
  focusHTML = `
<div style="background: var(--background-modifier-card); border-left: 4px solid ${nextLevel.color}; border-radius: 8px; padding: 1.2rem; margin-top: 1.5rem;">
  <div style="color: #94a3b8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;">⏭️ Поточний фокус</div>
  <div style="color: var(--text-normal); font-size: 1.2rem; font-weight: 700;">${nextLevel.icon} ${nextLevel.name}</div>
  <div style="color: ${nextLevel.color}; margin-top: 0.4rem;">Залишилося докласти: <strong>${fmt$(gap)}</strong> · Рівень ${nextLevel.level}</div>
</div>`;
}
dv.el('div', focusHTML);
```

---

## 📝 Журнал оновлень

| Дата       | Подія                             | Сума    | Інструмент            |
| ---------- | --------------------------------- | ------- | --------------------- |
| 2026-05-07 | Створено дашборд                  | $0      | —                     |
| 2026-06-06 | ОВДП → mono банка $5,000 (3%, миттєво); звільнені $600 → SGOV | — | ОВДП / SGOV |
| 2026-06-07 | Крипто-шматок: WhiteBIT (основна, UAH-рейки) + Binance (Earn). Транші instant/30д/90д | — | USDT / USDC |
| 2026-06-25 | Заміна SGOV/VGSH → UCITS Acc ETF: 0-1yr `IE00BGSF1X88` (Р2) + 0-1yr/1-3yr `IE00BYXPSP02` (Р3) | — | iShares UCITS |

> Додавай рядки знизу — звичайна Markdown-таблиця. Для дашборду використовуються Properties зверху файлу.

## 🔗 Зв'язані файли

- [[Стратегія побудови Emergency fund]] — стратегія, фази, правила використання
- [[Дослідження ОВДП]] — де купляти USD ОВДП
- [[Budget Allocation Dashboard]] — місячний бюджет (50/10/25/15)
- [[Capital Report]] — загальний капітал
