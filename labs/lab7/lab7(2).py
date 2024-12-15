import matplotlib.pyplot as plt
from collections import Counter


user_text = input("Введіть текст: ")


letters_only = [char.lower() for char in user_text if char.isalpha()]  
letter_counts = Counter(letters_only)  


letters = list(letter_counts.keys())
frequencies = list(letter_counts.values())


plt.figure(figsize=(10, 6))
plt.bar(letters, frequencies, color="skyblue", edgecolor="black")


plt.title("Частота появи літер у тексті", fontsize=14)
plt.xlabel("Літери", fontsize=12)
plt.ylabel("Кількість появ", fontsize=12)


plt.savefig("letter_frequency_histogram.png", format="png", dpi=300)
print("Гістограму збережено як letter_frequency_histogram.png")

plt.show()