import pandas as pd

# Початковий словник з практичної роботи №5
baggage = {
    1: (3, 45.0),
    2: (2, 32.5),
    3: (1, 20.0),
    4: (4, 50.5),
    5: (1, 27.0),
    6: (3, 42.0),
    7: (2, 28.0),
    8: (1, 24.5),
    9: (5, 63.0),
    10: (2, 26.0)
}

# Доповнимо словник новими записами
baggage[11] = (3, 41.0)
baggage[12] = (2, 33.5)

# Перетворення словника на DataFrame
df = pd.DataFrame.from_dict(
    baggage,
    orient='index',
    columns=['items', 'weight']
)

# Додамо новий стовпець – середня вага однієї речі
df['avg_item_weight'] = df['weight'] / df['items']

# Виведемо отриманий DataFrame
print("DataFrame:")
print(df, "\n")

# Перші 3 рядки DataFrame
print("Перші 3 рядки:")
print(df.head(3), "\n")

# Типи даних
print("Типи даних:")
print(df.dtypes, "\n")

# Кількість рядків і стовпців
print("Форма DataFrame (рядки, стовпці):")
print(df.shape, "\n")

# Описова статистика
print("Описова статистика:")
print(df.describe(), "\n")

# Фільтрація даних – вага > 30 кг
filtered = df[df['weight'] > 30]
print("Фільтрація: вага > 30 кг:")
print(filtered, "\n")

# Сортування даних – за спаданням ваги
sorted_df = df.sort_values(by='weight', ascending=False)
print("Сортування за вагою (спадання):")
print(sorted_df, "\n")

# Групування: середня вага для кожної кількості речей
grouped = df.groupby('items')['weight'].mean()
print("Групування: середня вага для кожної кількості речей:")
print(grouped, "\n")

# Додаткові агрегації
max_weight = df['weight'].max()
print("Максимальна вага багажу:", max_weight)

unique_items = df['items'].nunique()
print("Кількість унікальних значень 'items':", unique_items)
