# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen, Request
from urllib.parse import quote
from collections import Counter

def analyze_news_page(url):
    try:
        # Кодування URL для роботи з кирилицею
        encoded_url = quote(url, safe=':/')
        
        # Відправка запиту з User-Agent
        request = Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(request)
        html_content = response.read().decode('utf-8')

        # Виділення тексту між HTML-тегами
        text = re.sub(r'<[^>]+>', ' ', html_content)  # Видаляємо всі HTML-теги
        words = re.findall(r'\b\w+\b', text.lower())  # Виділення слів
        word_frequency = Counter(words)

        # Пошук HTML-тегів
        tags = re.findall(r'<(\w+)', html_content)  # Виділення імен тегів
        tags_frequency = Counter(tags)

        # Пошук посилань
        links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)', html_content)
        links_count = len(links)

        # Пошук зображень
        images = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)', html_content)
        images_count = len(images)

        # Результати аналізу
        return {
            "word_frequency": word_frequency.most_common(10),  # Топ 10 слів
            "tags_frequency": tags_frequency.most_common(10),  # Топ 10 тегів
            "links_count": links_count,
            "images_count": images_count
        }

    except Exception as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return None


# Демонстрація роботи
if __name__ == "__main__":
    url = input("Введіть URL сторінки новин: ")
    result = analyze_news_page(url)

    if result:
        print("\nЧастота появи слів (топ 10):")
        for word, freq in result["word_frequency"]:
            print(f"{word}: {freq}")

        print("\nЧастота HTML тегів (топ 10):")
        for tag, freq in result["tags_frequency"]:
            print(f"<{tag}>: {freq}")

        print(f"\nКількість посилань: {result['links_count']}")
        print(f"Кількість зображень: {result['images_count']}")