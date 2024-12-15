import os
import sys
import subprocess

LABS_DIR = 'labs'  

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

if __name__ == '__main__':
    main()