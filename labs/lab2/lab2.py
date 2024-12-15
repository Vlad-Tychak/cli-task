# -*- coding: utf-8 -*-

def poshuk_elementa(elements, search_element):
    if search_element in elements:
        return "Значення знайдено: {}".format(search_element)
    else:
        return "Значення не знайдено"


elements = ['телефон', 'бункер', 'табір', 'машина', 'стіл']


search_element = str(input('Введіть текст: ')).strip()


result = poshuk_elementa(elements, search_element)
print(result)