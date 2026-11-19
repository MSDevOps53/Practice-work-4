
# Автоматичне тестування програми
# Практична робота: Оброблення текстових файлів
# Варіант 6

import unittest
from process_file import format_line


class TestFileProcessing(unittest.TestCase):

    # Перевірка доповнення короткого рядка пробілами
    def test_short_line(self):
        result = format_line("Python")

        self.assertEqual(len(result), 20)
        self.assertEqual(result, "Python" + " " * 14)

    # Перевірка обрізання довгого рядка
    def test_long_line(self):
        result = format_line("Programming language Python")

        self.assertEqual(len(result), 20)
        self.assertEqual(result, "Programming language")

    # Перевірка рядка довжиною рівно 20 символів
    def test_exact_line(self):
        result = format_line("12345678901234567890")

        self.assertEqual(len(result), 20)
        self.assertEqual(result, "12345678901234567890")


if __name__ == "__main__":
    unittest.main()
