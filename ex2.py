import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv('comptage_velo_2010.csv')

# Перевірка основних характеристик
print(df.head())
print(df.info())
print(df.describe())

# 1. Загальна кількість велосипедистів за рік на всіх доріжках
numeric_cols = df.select_dtypes(include='number').columns
total_all = df[numeric_cols].sum().sum()

print("Загальна кількість велосипедистів за рік (усі велодоріжки):", total_all)

# 2. Загальна кількість велосипедистів за рік на кожній доріжці
total_per_path = df[numeric_cols].sum()
print("\nКількість велосипедистів за рік на кожній доріжці:")
print(total_per_path)

# 3. Найпопулярніший місяць на трьох велодоріжках

# Створення стовпця 'month'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['month'] = df['Date'].dt.month

paths = numeric_cols[:3]  

for path in paths:
    month_sum = df.groupby('month')[path].sum()
    popular_month = month_sum.idxmax()
    print(f"\nНайпопулярніший місяць для '{path}': {popular_month}")

# 4. Побудова графіка завантаженості велодоріжки Berri1
path_to_plot = "Berri1"

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

plt.figure(figsize=(16, 4))

plt.plot(df['Date'], df[path_to_plot], marker='.', markersize=3, linewidth=1)

plt.title(f'Завантаженість велодоріжки "{path_to_plot}" по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)

import calendar
months = range(1, 13)
month_starts = [pd.Timestamp(year=2010, month=m, day=1) for m in months]
month_labels = [calendar.month_name[m] for m in months]

plt.xticks(month_starts, month_labels, rotation=45)

plt.tight_layout()
plt.savefig("berri1_monthly_plot.png")
plt.show()
