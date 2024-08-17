import unittest
from unittest import TestCase

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.entrypoints.cli.main import main
from src.pytemplate.service.calculator import Calculator


class TestOperands(TestCase):
    def test_types(self):
        self.assertIsInstance(Operands(first_operand=1, second_operand=1), Operands)

    def test_operands_factory(self):
        operands = operands_factory(first_operand=1, second_operand=1)
        self.assertIsInstance(operands, Operands)
        self.assertEqual(operands.first_operand, 1)
        self.assertEqual(operands.second_operand, 1)


class Testcalculator(TestCase):
    def test_add(self):
        calculator = Calculator()
        operands = Operands(first_operand=1, second_operand=1)
        self.assertEqual(calculator.add(operands), 2)

    def test_subtract(self):
        calculator = Calculator()
        operands = Operands(first_operand=1, second_operand=1)
        self.assertEqual(calculator.subtract(operands), 0)

    def test_multiply(self):
        calculator = Calculator()
        operands = Operands(first_operand=2, second_operand=3)
        self.assertEqual(calculator.multiply(operands), 6)

    def test_divide(self):
        calculator = Calculator()
        operands = Operands(first_operand=1, second_operand=1)
        self.assertEqual(calculator.divide(operands), 1)


class TestMain(TestCase):
    def test_main(self):
        self.assertEqual(main(1, 1, "add"), 2)
        self.assertEqual(main(1, 1, "subtract"), 0)
        self.assertEqual(main(2, 3, "multiply"), 6)
        self.assertEqual(main(1, 1, "divide"), 1)


if __name__ == "__main__":
    unittest.main()
