"""Частина б): підрахунок слів різної довжини (учасник 1)."""

import re

# За умовою довжина кожного слова не повинна перевищувати 16 символів.
MAX_LENGTH = 16


def get_words(text):
    """Повертає слова, відокремлюючи їх пробілами та розділовими знаками."""
    # Регулярний вираз знаходить послідовності літер (у т. ч. українських).
    # Цифри, пробіли та розділові знаки не входять до складу слів.
    return re.findall(r"[^\W\d_]+", text, flags=re.UNICODE)


def count_words(text):
    """Групує всі входження слів за кількістю символів від 1 до 16."""
    # Словник: ключ — довжина слова, значення — список слів цієї довжини.
    groups = {length: [] for length in range(1, MAX_LENGTH + 1)}

    for word in get_words(text):
        length = len(word)
        if length > MAX_LENGTH:
            # Замість непомітного пропуску слова повідомляємо про порушення умови.
            raise ValueError(f"Слово «{word}» має {length} символів (максимум 16).")
        groups[length].append(word)

    return groups


def process_file(source_name, result_name):
    """Читає TF4_1.txt, рахує слова та записує 16 рядків до TF4_2.txt."""
    try:
        # Читаємо весь вміст першого файлу.
        with open(source_name, "r", encoding="utf-8") as source:
            text = source.read()

        groups = count_words(text)

        # Створюємо файл із результатами обробки.
        with open(result_name, "w", encoding="utf-8") as result:
            for length in range(1, MAX_LENGTH + 1):
                words = groups[length]
                count = len(words)  # Ураховуємо й повторення однакових слів.
                example = words[0] if words else "немає"

                # Правильно відмінюємо слово «символ» (1, 2–4, 5–16).
                unit = "символ" if length == 1 else ("символи" if length in (2, 3, 4) else "символів")

                # Один рядок — одна довжина слова.
                result.write(f"{length} {unit} | слово: {example} | кількість: {count}\n")

        print(f"Обробку завершено. Результат записано у {result_name}.")
        return True

    except FileNotFoundError:
        print(f"Помилка: не знайдено файл {source_name}.")
        return False
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Помилка обробки файлів: {error}")
        return False
