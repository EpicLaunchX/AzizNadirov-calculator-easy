import unittest
from unittest import TestCase

from src.pytemplate.domain.models import Operands, operands_factory


class TestOperands(TestCase):
    def test_types(self):
        self.assertIsInstance(Operands(first_operand=1, second_operand=1), Operands)

    def test_operands_factory(self):
        operands = operands_factory(first_operand=1, second_operand=1)
        self.assertIsInstance(operands, Operands)
        self.assertEqual(operands.first_operand, 1)
        self.assertEqual(operands.second_operand, 1)


if __name__ == "__main__":
    unittest.main()
