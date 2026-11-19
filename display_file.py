"""Частина в): читання та виведення результату (учасник 2)."""


def display_file(file_name):
    """Відображає файл результату по рядках."""
    try:
        print(f"\nВміст файлу {file_name}:")

        # Використовуємо цикл по файлу, щоб друкувати саме по рядках.
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                print(line.rstrip("\n"))

        return True

    except FileNotFoundError:
        print(f"Помилка: не знайдено файл {file_name}.")
        return False
    except (OSError, UnicodeError) as error:
        print(f"Помилка читання файлу {file_name}: {error}")
        return False
