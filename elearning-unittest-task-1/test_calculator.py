"""Docstring."""

import unittest
from tasks.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Docstring."""

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 2), 4)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3,3),9)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(6,3),3)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6,3),2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(36),6)

    def test_pi(self):
        self.assertEqual(self.calculator.pi(3),0.05)


if __name__ == "__main__":
    unittest.main()
