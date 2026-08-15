import csv
import glob
import json
import math
import os
import re
from collections import Counter, defaultdict
from statistics import median, mean

ROOT = '/tmp/dou-salaries/data'
# Use one mini file per survey. The latest repository survey is 2020_june_mini.csv.
paths = []
for path in glob.glob(os.path.join(ROOT, '*_mini.csv')):
    base = os.path.basename(path)
    if base == '2020_june_mini.csv' or base.endswith('_dec_mini.csv') or base.endswith('_june_mini.csv') or base.endswith('_may_mini.csv'):
        paths.append(path)

period_order = lambda p: (int(p.split('-')[0]), {'may': 5, 'june': 6, 'dec': 12}.get(p.split('-')[1], 0))


def q(xs, pct):
    xs = sorted(xs)
    if not xs:
        return None
    idx = (len(xs) - 1) * pct
    lo, hi = int(math.floor(idx)), int(math.ceil(idx))
    return xs[lo] if lo == hi else xs[lo] + (xs[hi] - xs[lo]) * (idx - lo)


def profile(rows):
    salaries = [x['salary'] for x in rows]
    return {
        'n': len(rows), 'median': round(median(salaries)), 'p25': round(q(salaries, .25)),
        'p75': round(q(salaries, .75)), 'p90': round(q(salaries, .90)),
        'mean': round(mean(salaries)), 'share_6000_plus_pct': round(100 * sum(x >= 6000 for x in salaries) / len(salaries), 1)
    }

all_rows=[]
for path in paths:
    basename=os.path.basename(path)
    m=re.match(r'(\d{4})_(may|june|dec)_mini\.csv', basename)
    if not m:
        continue
    period=f'{m.group(1)}-{m.group(2)}'
    with open(path, encoding='utf-8-sig', newline='') as fh:
        for row in csv.DictReader(fh):
            lang=(row.get('Язык.программирования') or '').strip()
            if 'C#' not in lang and '.NET' not in lang:
                continue
            try:
                sal=float(row['Зарплата.в.месяц'])
                exp=float(row['exp'])
            except (ValueError, TypeError, KeyError):
                continue
            if sal <= 0 or sal > 50000:
                continue
            all_rows.append({
                'period': period, 'salary': sal, 'exp': exp,
                'role': (row.get('Должность') or '').strip(),
                'city': (row.get('Город') or '').strip(),
                'english': (row.get('Уровень.английского') or '').strip(),
                'company_type': (row.get('Тип.компании') or '').strip(),
                'company_size': (row.get('Размер.компании') or '').strip(),
            })

by_period=defaultdict(list)
for r in all_rows:
    by_period[r['period']].append(r)
series={p:profile(rows) for p,rows in sorted(by_period.items(), key=lambda kv: period_order(kv[0]))}
latest_period=max(by_period, key=period_order)
latest=by_period[latest_period]

by_role=defaultdict(list)
for r in latest:
    by_role[r['role']].append(r)
roles={role: profile(rows) for role,rows in by_role.items() if len(rows)>=15}
roles=dict(sorted(roles.items(), key=lambda kv:(-kv[1]['median'], -kv[1]['n'])))

bands=[('0–2',0,2),('2–4',2,4),('4–6',4,6),('6–8',6,8),('8–10',8,10),('10+',10,99)]
experience={label: profile([r for r in latest if low <= r['exp'] < high]) for label,low,high in bands if any(low <= r['exp'] < high for r in latest)}

high=[r for r in latest if r['salary'] >= 6000]
def distribution(rows, field):
    return [{'value':k or '(empty)','n':v,'share_pct':round(100*v/len(rows),1)} for k,v in Counter(r[field] for r in rows).most_common(10)]

result={
 'source': 'imax/dou-salaries, raw/mini survey CSVs',
 'latest_period': latest_period,
 'latest_net_profile': profile(latest),
 'net_salary_series': series,
 'latest_roles_n_ge_15': roles,
 'latest_experience_bands': experience,
 'latest_6000_plus_n': len(high),
 'latest_6000_plus_by_role': distribution(high,'role'),
 'latest_6000_plus_by_english': distribution(high,'english'),
 'latest_6000_plus_by_company_type': distribution(high,'company_type'),
 'caveats': [
   'Repository latest raw/mini data is June 2020, despite GitHub metadata showing a later repository update.',
   'Survey is self-reported and cross-sectional; it is not a current 2026 salary dataset.',
   'C#/.NET is detected from the programming-language field; role labels come from survey respondents.'
 ]
}
print(json.dumps(result, ensure_ascii=False, indent=2))
