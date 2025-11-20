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
df['Date'] = pd.to_datetime(df['Date'])

df_berri = df[['Date', 'Berri1']].dropna()

# Побудова графіка
plt.figure(figsize=(12,6))
plt.plot(df_berri['Date'], df_berri['Berri1'], marker='o', linestyle='-', markersize=3)

plt.title("Завантаженість велодоріжки Berri1 протягом 2010 року")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)

months = mdates.MonthLocator()                  
months_fmt = mdates.DateFormatter('%b')   

ax = plt.gca()
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(months_fmt)

plt.tight_layout()

plt.savefig("berri1_plot.png", dpi=300)

plt.show()
