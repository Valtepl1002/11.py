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

# 3. Найпопулярніший місяць на вибраних трьох велодоріжках

# Створення стовпця 'month'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['month'] = df['Date'].dt.month

# Обери три назви своїх доріжок зі стовпців
paths = numeric_cols[:3]  

for path in paths:
    month_sum = df.groupby('month')[path].sum()
    popular_month = month_sum.idxmax()
    print(f"\nНайпопулярніший місяць для '{path}': {popular_month}")

# 4. Побудова графіка завантаженості однієї велодоріжки
path_to_plot = numeric_cols[0]   # Вибери потрібну доріжку
monthly_counts = df.groupby('month')[path_to_plot].sum()

plt.figure(figsize=(10,5))
monthly_counts.plot(kind='line', marker='o')
plt.title(f'Завантаженість велодоріжки "{path_to_plot}" по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)
plt.show()

# Вибрана велодоріжка
path_to_plot = "Berri1"

# Переконаємось, що дата у форматі datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['month'] = df['Date'].dt.month

# Помісячні суми
monthly_counts = df.groupby('month')[path_to_plot].sum()

# Створення файлу
monthly_df = monthly_counts.reset_index()
monthly_df.columns = ["Month", "Cyclists"]

output_filename = f"monthly_load_{path_to_plot}.csv"
monthly_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"\nФайл '{output_filename}' успішно створено!")
print(monthly_df)

# Побудова графіка
plt.figure(figsize=(10,5))
monthly_counts.plot(kind='line', marker='o')
plt.title(f'Завантаженість велодоріжки "{path_to_plot}" по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)
plt.show()
