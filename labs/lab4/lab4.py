# -*- coding: utf-8 -*-
import re

def analyze_sentences(text):
   
    sentences = re.split(r'[.!?…]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]  
    

    total_sentences = len(sentences)
    

    exclamatory_sentences = len(re.findall(r'!', text))
    

    interrogative_sentences = len(re.findall(r'\?', text))
    

    ellipsis_sentences = len(re.findall(r'\.\.\.', text))
    
    return total_sentences, exclamatory_sentences, interrogative_sentences, ellipsis_sentences



user_text = input("Введіть текст: ")


total, exclamatory, interrogative, ellipsis = analyze_sentences(user_text)


print(f"Загальна кількість речень: {total}")
print(f"Кількість окличних речень: {exclamatory}")
print(f"Кількість питальних речень: {interrogative}")
print(f"Кількість речень, що закінчуються трикрапкою: {ellipsis}")