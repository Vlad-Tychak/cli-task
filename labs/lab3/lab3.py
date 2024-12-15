# -*- coding: utf-8 -*-
import os


def create_group_file(group_name, students):
    with open(f"{group_name}.txt", "w", encoding="utf-8") as file:
        for student, grade in students.items():
            file.write(f"{student},{grade}\n")


def append_to_group_file(group_name, students):
    with open(f"{group_name}.txt", "a", encoding="utf-8") as file:
        for student, grade in students.items():
            file.write(f"{student},{grade}\n")

def read_group_file(group_name):
    try:
        with open(f"{group_name}.txt", "r", encoding="utf-8") as file:
            data = file.readlines()
        return [line.strip().split(",") for line in data]
    except FileNotFoundError:
        print(f"Файл для групи {group_name} не знайдено.")
        return []

def search_file_in_directory(directory, filename):
    return filename in os.listdir(directory)


def search_student_in_file(group_name, student_name):
    data = read_group_file(group_name)
    for student, grade in data:
        if student == student_name:
            return float(grade)
    return None

def sort_group_file_by_grade(group_name):
    data = read_group_file(group_name)
    sorted_data = sorted(data, key=lambda x: float(x[1]), reverse=True)
    with open(f"{group_name}.txt", "w", encoding="utf-8") as file:
        for student, grade in sorted_data:
            file.write(f"{student},{grade}\n")
    return sorted_data

def interactive_mode():
    while True:
        print("\nМеню:")
        print("1. Створити файл групи")
        print("2. Додати студентів у файл групи")
        print("3. Показати дані групи")
        print("4. Знайти середній бал студента")
        print("5. Відсортувати дані у файлі за середнім балом")
        print("6. Перевірити наявність файлу в каталозі")
        print("7. Вийти")
        
        choice = input("Оберіть дію: ")
        
        if choice == "1":
            group_name = input("Введіть назву групи: ")
            students = {}
            print("Введіть дані студентів (ім'я та середній бал). Введіть 'stop', щоб завершити.")
            while True:
                name = input("Ім'я студента: ")
                if name.lower() == "stop":
                    break
                grade = input("Середній бал: ")
                students[name] = float(grade)
            create_group_file(group_name, students)
            print(f"Файл для групи '{group_name}' створено.")
        
        elif choice == "2":
            group_name = input("Введіть назву групи: ")
            students = {}
            print("Введіть дані студентів (ім'я та середній бал). Введіть 'stop', щоб завершити.")
            while True:
                name = input("Ім'я студента: ")
                if name.lower() == "stop":
                    break
                grade = input("Середній бал: ")
                students[name] = float(grade)
            append_to_group_file(group_name, students)
            print(f"Дані додано до файлу групи '{group_name}'.")
        
        elif choice == "3":
            group_name = input("Введіть назву групи: ")
            data = read_group_file(group_name)
            if data:
                print("Дані групи:")
                for student, grade in data:
                    print(f"{student}: {grade}")
        
        elif choice == "4":
            group_name = input("Введіть назву групи: ")
            student_name = input("Введіть ім'я студента: ")
            grade = search_student_in_file(group_name, student_name)
            if grade is not None:
                print(f"Середній бал студента {student_name}: {grade}")
            else:
                print(f"Студента {student_name} не знайдено у групі {group_name}.")
        
        elif choice == "5":
            group_name = input("Введіть назву групи: ")
            sorted_data = sort_group_file_by_grade(group_name)
            print("Дані групи відсортовано:")
            for student, grade in sorted_data:
                print(f"{student}: {grade}")
        
        elif choice == "6":
            filename = input("Введіть назву файлу (з розширенням .txt): ")
            if search_file_in_directory(".", filename):
                print(f"Файл '{filename}' існує в каталозі.")
            else:
                print(f"Файл '{filename}' не знайдено.")
        
        elif choice == "7":
            print("Вихід із програми.")
            break
        
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    interactive_mode()