---
title: Методика аналізу raw salary-даних DOU (devua/csv)
created: 2026-08-18
updated: 2026-08-18
type: guide
status: active
tags: [research, salary, dou, methodology]
sources: [https://github.com/devua/csv/tree/master/salaries]
---

# Методика аналізу raw salary-даних DOU (devua/csv)

## Джерело
- Основний датасет: [devua/csv/salaries (GitHub)](https://github.com/devua/csv/tree/master/salaries).
- Дані у форматі CSV, окремий файл для кожного періоду (`2026_june_raw.csv`, `2026_march_raw.csv` тощо).
- Покриває всі основні тайтли та технології (Backend, Frontend/React/Angular/Vue, QA, DevOps, Data тощо).

## Як виконувати аналіз
1. Обрати потрібну категорію — наприклад, `Категорії = Software Engineering & Architecture`,
   `Основна мова програмування = C# / .NET` або `Frontend/React/JavaScript/TypeScript`.
2. Відфільтрувати некоректні рядки (наприклад, salary < $100 чи > $50k, пусті значення чи нетипові тайтли).
3. Вказати:
   - Який період
   - Які конкретно поля використано
   - Які критерії входження
4. Порахувати метрики (median, P75, P90, частка $5k+, $6k+ та інше).
5. Для кожного нового стеку/тайтлу — робити окремий research-файл (наприклад, .NET, Frontend/React, QA, Java).
6. Вказувати: лінк на методичку, лінк на raw-дані, зберігати provenance.
7. Додається короткий python-скрипт (див. нижче).

## Python-приклад для відтворюваності

```python
# analyze_current_dou_salary.py: Загальна схема аналізу
import pandas as pd
DATA_PATH = "/tmp/devua-csv/salaries/2026_june_raw.csv"
df = pd.read_csv(DATA_PATH)
df = df[df['Категорії'] == 'Software Engineering & Architecture']
df = df[df['Основна мова програмування'].str.contains("React|Frontend|JavaScript|TypeScript", na=False)]
df = df[(df['Зарплата'] > 100) & (df['Зарплата'] < 50000)]

print(f"N={len(df)}")
for col in ['Зарплата']:
    print(f"Median: {df[col].median()}")
    print(f"P75: {df[col].quantile(0.75)}")
    print(f"P90: {df[col].quantile(0.9)}")
    print(f"$5k+: {round(100 * (df[col] >= 5000).sum() / len(df), 1)}%")
    print(f"$6k+: {round(100 * (df[col] >= 6000).sum() / len(df), 1)}%")
```

## Де згадувати
- Всі датовані аналізи salary ринку по стеку (наприклад, .NET, Frontend, QA тощо) —
  у research/ з посиланням на цю методичку і на сам raw-датасет.
- Сторінка оновлюється лише при зміні методу, структурування, типу вхідних файлів чи логіки розрахунку.

## Для чого це зроблено
- Відірвані огляди або топ-листи не дають коректної картини.
- Методика забезпечує повторюваність, верифікованість і швидкий аудит для будь-якого напрямку (технології / seniority).

---
**Обиратимеш стек та період — даси команду, і результат буде прозорий і співставний по всіх напрямках.**