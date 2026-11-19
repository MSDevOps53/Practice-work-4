"""Невеликі автоматизовані перевірки програми (стандартний unittest)."""

import os
import tempfile
import unittest

from create_file import create_file
from display_file import display_file
from process_file import count_words, get_words, process_file


class TestTextFiles(unittest.TestCase):
    def test_split_punctuation(self):
        self.assertEqual(get_words("Я, ти! Код; слово."), ["Я", "ти", "Код", "слово"])

    def test_count_and_repetitions(self):
        groups = count_words("Я, я! код код; море.")
        self.assertEqual(len(groups[1]), 2)
        self.assertEqual(len(groups[3]), 2)
        self.assertEqual(len(groups[4]), 1)

    def test_max_length(self):
        self.assertEqual(len(count_words("мікропроцесорний")[16]), 1)
        with self.assertRaises(ValueError):
            count_words("електрообладнання")  # 17 символів

    def test_files_and_output(self):
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, "TF4_1.txt")
            result = os.path.join(folder, "TF4_2.txt")
            self.assertTrue(create_file(source))
            self.assertTrue(process_file(source, result))
            self.assertTrue(display_file(result))
            with open(result, encoding="utf-8") as file:
                lines = file.readlines()
            self.assertEqual(len(lines), 16)
            self.assertIn("16 символів | слово: мікропроцесорний | кількість: 1", lines[15])

    def test_missing_input_file(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertFalse(process_file(os.path.join(folder, "not_exist.txt"),
                                          os.path.join(folder, "result.txt")))


if __name__ == "__main__":
    unittest.main()
