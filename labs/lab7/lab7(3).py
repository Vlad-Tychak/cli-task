import matplotlib.pyplot as plt


user_text = input("Введіть текст: ")


def count_sentence_types(text):
    normal = text.count(".") - text.count("...")  
    exclamatory = text.count("!")  
    interrogative = text.count("?")  
    ellipsis = text.count("...")  
    return {"Звичайні": normal, "Питальні": interrogative, "Окличні": exclamatory, "Трикрапка": ellipsis}


sentence_counts = count_sentence_types(user_text)


categories = list(sentence_counts.keys())
counts = list(sentence_counts.values())


plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color=["blue", "green", "red", "purple"], edgecolor="black")


plt.title("Частота появи різних типів речень", fontsize=14)
plt.xlabel("Типи речень", fontsize=12)
plt.ylabel("Кількість речень", fontsize=12)


plt.savefig("sentence_type_histogram.png", format="png", dpi=300)
print("Гістограму збережено як sentence_type_histogram.png")

plt.show()