import unittest
from unittest import TestCase

from src.pytemplate.domain.models import Operands


class TestOperands(TestCase):
    def test_types(self):
        self.assertIsInstance(Operands(1, 1), Operands)


if __name__ == "__main__":
    unittest.main()
