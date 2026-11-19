
# Частина в) Виведення вмісту файлу
# Практична робота: Оброблення текстових файлів
# Варіант 6

from create_file import Open


# Функція читання та виведення результату
def print_file(file_name):
    file = Open(file_name, "r")

    if file is None:
        return False

    print("\nNew sequence:")

    for line in file:
        print("|" + line.rstrip("\r\n") + "|")

    file.close()

    print("File " + file_name + " was closed!")

    return True
