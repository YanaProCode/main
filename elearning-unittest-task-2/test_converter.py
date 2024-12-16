"""Docstring."""

import unittest
from unittest.mock import patch
from task.converter import Converter


def mock_converter(_, celsius):
    return celsius * 9.0 / 5.0 + 32


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    @patch('task.converter.Converter.convert_celsius_to_fahrenheit', new=mock_converter)
    def test_converter(self):
        celsius_value = 20
        expected_fahrenheit_value = mock_converter(None, celsius_value)
        self.assertEqual(self.converter.convert_celsius_to_fahrenheit(celsius_value), expected_fahrenheit_value)


if __name__ == "__main__":
    unittest.main()
