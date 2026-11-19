
# Частина б) Оброблення текстових рядків
# Практична робота: Оброблення текстових файлів
# Варіант 6

from create_file import Open


# Функція форматування рядка до 20 символів
def format_line(line):
    return line.ljust(20)[:20]


# Функція оброблення файлів
def process_file(file1_name, file2_name):
    file_r = Open(file1_name, "r")

    if file_r is None:
        return False

    file_w = Open(file2_name, "w")

    if file_w is None:
        file_r.close()
        return False

    for line in file_r:
        # Видалення символів переходу на новий рядок
        line = line.rstrip("\r\n")

        # Формування рядка довжиною 20 символів
        new_line = format_line(line)

        # Запис результату у другий файл
        file_w.write(new_line + "\n")

    file_r.close()
    file_w.close()

    print("Information was successfully added to " + file2_name + "!")
    print("Files were closed!")

    return True
