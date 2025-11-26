# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.
# Також візьміть до уваги наступні умови:

# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка:
# шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

# 2. Рекурсивне читання директорій:
# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.

# 3. Копіювання файлів:

# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.

import os
import shutil
import argparse
from pathlib import Path


def copy_and_sort_files(src_dir, dest_dir="dist"):
    """Recursively copy files from src_dir to dest_dir,
    sort them into subdirs by file extension."""
    count = 0

    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                count += copy_and_sort_files(item_path, dest_dir)
            elif os.path.isfile(item_path):

                file_extension = Path(item).suffix[1:] or "no_extension"
                file_extension = file_extension.lower().replace(".", "")
                target_dir = os.path.join(dest_dir, file_extension)

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir, exist_ok=True)

                if not os.path.exists(os.path.join(target_dir, item)):
                    shutil.copy2(item_path, target_dir)
                    count += 1

    except Exception as e:
        print(f"Error processing {src_dir}: {e}")
    return count


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Copy and sort files by extension.")
    parser.add_argument("src_dir", help="Source directory to copy files from.")
    parser.add_argument(
        "dest_dir",
        nargs="?",
        default="dist",
        help="Destination directory to copy files to (default: dist).",
    )
    args = parser.parse_args()

    files_copied = copy_and_sort_files(args.src_dir, args.dest_dir)

    print(f"Total files copied: {files_copied} to {args.dest_dir}")

# Example usage:
# python.exe c:/src/GoIt/goit-algo-hw-03/dir_contetnt_sort.py "c:\src\GoIt\BasicAlgorithms&DataStructures\" "c:\src\GoIt\BasicAlgorithms&DataStructures\dist_test"
