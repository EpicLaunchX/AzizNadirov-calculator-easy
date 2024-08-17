import unittest
from unittest import TestCase

from src.pytemplate.domain.models import Operands


class TestOperands(TestCase):
    def test_types(self):
        self.assertIsInstance(Operands(first_operand=1, second_operand=1), Operands)


if __name__ == "__main__":
    unittest.main()
