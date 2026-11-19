"""Практична робота №4, варіант №3. Оброблення текстових файлів."""

# Кожна частина завдання написана як окремий модуль.
from create_file import create_file
from process_file import process_file
from display_file import display_file


# Імена файлів відповідно до варіанта №3.
SOURCE_FILE = "TF4_1.txt"
RESULT_FILE = "TF4_2.txt"


def main():
    """Послідовно виконує частини а), б) та в)."""
    # а) Створюємо файл із рядками та словами різної довжини.
    if not create_file(SOURCE_FILE):
        return  # У разі помилки припиняємо роботу.

    # б) Читаємо перший файл та створюємо другий файл із підрахунками.
    if not process_file(SOURCE_FILE, RESULT_FILE):
        return

    # в) Читаємо другий файл та виводимо його по рядках.
    display_file(RESULT_FILE)


# Основна функція запускається лише під час виконання main.py.
if __name__ == "__main__":
    main()
