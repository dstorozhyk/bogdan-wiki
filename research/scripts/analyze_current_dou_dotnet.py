import csv, json, math, os
from collections import Counter, defaultdict
from statistics import median

ROOT = '/tmp/devua-csv/salaries'
FILES = ['2025_june_raw.csv', '2025_dec_raw.csv', '2026_june_raw.csv']


def first(row, candidates):
    for key in candidates:
        if key in row and row[key] is not None:
            return row[key].strip()
    return ''


def parse_num(value):
    try:
        return float((value or '').replace('$', '').replace(',', '').replace(' ', '').strip())
    except ValueError:
        return None


def quantile(values, p):
    values = sorted(values)
    idx = (len(values) - 1) * p
    low, high = int(idx), math.ceil(idx)
    return values[low] if low == high else values[low] + (values[high] - values[low]) * (idx - low)


def stats(rows):
    values = [row['salary'] for row in rows]
    return {
        'n': len(values), 'median': round(median(values)), 'p25': round(quantile(values, .25)),
        'p75': round(quantile(values, .75)), 'p90': round(quantile(values, .90)),
        'share_6000_plus_pct': round(100 * sum(value >= 6000 for value in values) / len(values), 1),
    }


rows = []
for name in FILES:
    path = os.path.join(ROOT, name)
    encoding = 'cp1251' if name == '2025_june_raw.csv' else 'utf-8-sig'
    with open(path, encoding=encoding, newline='') as handle:
        for record in csv.DictReader(handle):
            language = first(record, ['Основна мова програмування']).replace(' ', '')
            category = first(record, ['Категорії', 'Категорія'])
            salary = parse_num(first(record, [
                'ЗАРПЛАТА СУМАРНИЙ ДОХІД в ІТ',
                'ЗАРПЛАТА / СУМАРНИЙ ДОХІД в IT у $$$ за місяць, лише ставка \nЧИСТИМИ - після сплати податків',
            ]))
            if language not in {'C#/.NET', 'C#NET'} or category not in {'SE', 'Software Engineering & Architecture'}:
                continue
            if salary is None or not 100 <= salary <= 50000:
                continue
            rows.append({
                'period': name.replace('_raw.csv', '').replace('_', '-'),
                'salary': salary,
                'title': first(record, ['Title_clean', 'Тайтл']),
                'role': first(record, ['Посади', 'Почніть вводити і оберіть вашу ОСНОВНУ посаду зі списку']),
                'experience': first(record, ['Загальний стаж роботи за нинішньою ІТ-спеціальністю']),
                'english': first(record, ['Знання англійської мови']),
            })

by_period = defaultdict(list)
for row in rows:
    by_period[row['period']].append(row)
latest = by_period['2026-june']
by_title = defaultdict(list)
for row in latest:
    by_title[row['title']].append(row)
high = [row for row in latest if row['salary'] >= 6000]

result = {
    'series': {period: stats(group) for period, group in by_period.items()},
    'latest_net': stats(latest),
    'title_stats_n_ge_10': {title: stats(group) for title, group in by_title.items() if len(group) >= 10},
    'high_n': len(high),
    'high_by_title': Counter(row['title'] for row in high).most_common(),
}
print(json.dumps(result, ensure_ascii=False, indent=2))
