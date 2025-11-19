# Імпорт бібліотек 
import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('stopwords')

# Читання локального файлу у репозиторії
with open("milton-paradise.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Токенізація
words = nltk.word_tokenize(text)

# 1. Кількість слів
print("Кількість слів у тексті:", len(words))

# 2. Топ-10 слів до очищення
freq_dist = FreqDist(w.lower() for w in words)
top10 = freq_dist.most_common(10)
print("\n10 найбільш вживаних слів (до очищення):")
print(top10)

# Графік топ-10 до очищення
plt.figure(figsize=(10,5))
plt.bar([w for w, c in top10], [c for w, c in top10])
plt.title("Топ-10 слів у тексті (до очищення)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()

# 3. Очищення тексту (стоп-слова + пунктуація) 
stop_words = set(stopwords.words("english"))
punct = set(string.punctuation)

clean_words = [
    w.lower() for w in words
    if w.lower() not in stop_words and
       w not in punct and
       w.isalpha()
]

# Топ-10 після очищення
freq_clean = FreqDist(clean_words)
top10_clean = freq_clean.most_common(10)
print("\n10 найбільш вживаних слів (після очищення):")
print(top10_clean)

# Графік після очищення 
plt.figure(figsize=(10,5))
plt.bar([w for w, c in top10_clean], [c for w, c in top10_clean])
plt.title("Топ-10 слів (після видалення стоп-слів та пунктуації)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()
