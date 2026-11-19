
# Частина а) Створення текстового файлу
# Практична робота: Оброблення текстових файлів
# Варіант 6


# Функція відкриття файлу з обробкою помилок
def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except OSError:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


# Функція створення початкового файлу
def create_file(file_name):
    file = Open(file_name, "w")

    if file is None:
        return False

    # Символьні рядки різної довжини
    lines = [
        "Python",
        "Text file processing",
        "Programming language Python is very interesting",
        "Sumy State University",
        "Hello world!"
    ]

    for line in lines:
        file.write(line + "\n")

    file.close()

    print("Information was successfully added to " + file_name + "!")
    print("File " + file_name + " was closed!")

    return True
