Цей код є скриптом для роботи з лабораторними роботами у вигляді Python-файлів, які зберігаються в певній директорії. Код реалізує простий CLI (Command Line Interface), який дозволяє виконувати дві основні операції:
Перегляд лабораторних робіт (list).
Запуск лабораторної роботи або конкретного завдання в межах лабораторної роботи (run).
Розглянемо, як працює кожна частина коду:
1. Імпорт бібліотек
import os
import sys
import subprocess
os: використовується для роботи з операційною системою, зокрема для доступу до файлової системи.
sys: дає доступ до аргументів командного рядка (через sys.argv) та для коректного завершення програми.
subprocess: дозволяє запускати інші програми (у даному випадку Python-скрипти) з вашого коду.
2. Константа LABS_DIR
LABS_DIR = 'labs'
Це константа, яка містить шлях до директорії, в якій зберігаються всі лабораторні роботи.
 Функція list_labs
def list_labs():
    """Вивести список лабораторних робіт."""
    labs = os.listdir(LABS_DIR)
    for lab in labs:
        if os.path.isdir(os.path.join(LABS_DIR, lab)):
            lab_files = os.listdir(os.path.join(LABS_DIR, lab))
            lab_files = [file for file in lab_files if file.endswith('.py')]
            print(f"{lab}: {', '.join(lab_files)}")
        else:
            print(f"{lab}: {', '.join([lab])}")
Функція list_labs виводить список лабораторних робіт, які знаходяться в директорії labs.
Для кожної лабораторної роботи перевіряється, чи це директорія. Якщо так, то вона перебирає файли в цій директорії, фільтруючи лише файли з розширенням .py (Python-скрипти), і виводить їх.
Якщо це не директорія, виводить просто ім'я файлу.
4. Функція run_lab
   def run_lab(lab_number, task_number=None):
    """Запуск лабораторної роботи."""
    lab_dir = os.path.join(LABS_DIR, f"lab{lab_number}")

    if os.path.isdir(lab_dir):
        lab_files = [f for f in os.listdir(lab_dir) if f.endswith('.py')]
        lab_files = sorted(lab_files)

        if task_number:
            task_file = f"lab{lab_number}({task_number}).py"
            if task_file in lab_files:
                print(f"Запуск лабораторної роботи {lab_number}, завдання {task_number}...")
                subprocess.run(['python3', os.path.join(lab_dir, task_file)])
            else:
                print(f"Завдання {task_number} не знайдено в лабораторній роботі {lab_number}.")
        else:
            for lab_file in lab_files:
                print(f"Запуск лабораторної роботи {lab_number}, файл {lab_file}...")
                subprocess.run(['python3', os.path.join(lab_dir, lab_file)])
    else:
        print(f"Лабораторна робота lab{lab_number} не знайдена.")

Функція run_lab запускає лабораторну роботу або завдання у вигляді Python-скрипта.
Вона отримує номер лабораторної роботи (lab_number) і необов'язковий параметр для завдання (task_number).
Спочатку перевіряється, чи існує директорія для цієї лабораторної роботи.
Потім перевіряється, чи є завдання в списку файлів. Якщо передано завдання, воно шукається серед файлів. Якщо завдання знайдене, виконується Python-скрипт для цього завдання.
Якщо завдання не передано, запускаються всі скрипти лабораторної роботи.
Якщо лабораторна робота або завдання не знайдено, виводиться відповідне повідомлення.
5. Основна функція main

def main():
    """Основна функція CLI."""
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть команду (list або run <lab_number> [<task_number>])")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'list':
        list_labs()

    elif command == 'run':
        if len(sys.argv) < 3:
            print("Будь ласка, вкажіть номер лабораторної роботи для запуску.")
            sys.exit(1)

        lab_number = sys.argv[2]

        task_number = int(sys.argv[3]) if len(sys.argv) > 3 else None
        run_lab(lab_number, task_number)

    else:
        print("Невідома команда. Доступні команди: list, run <lab_number> [<task_number>].")
        sys.exit(1)
  Основна функція main відповідає за обробку команд, введених через командний рядок.
Перевіряє, чи вказано хоча б одну команду.
Якщо команда list, викликається функція list_labs для виведення списку лабораторних робіт.
Якщо команда run, перевіряється наявність номеру лабораторної роботи і можливе завдання. Якщо вони є, викликається функція run_lab для запуску відповідного файлу.
Якщо команда не розпізнана, виводиться повідомлення про помилку.
6. Запуск програми
if name == '__main__':
    main()

Перевіряється, чи виконується цей файл як основний скрипт, і якщо так, викликається функція main.
Як використовувати цей код:
Перегляд лабораторних робіт: Для перегляду списку лабораторних робіт потрібно виконати команду:
python script_name.py list --- Запуск лабораторної роботи або завдання:
Для запуску лабораторної роботи:
python script_name.py run <lab_number> <task_number>
    
