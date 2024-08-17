from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main(first_operand: int, second_operand: int, action: str) -> int:
    """entry point of calc"""

    calc = Calculator()

    ops = {"add": calc.add, "subtract": calc.subtract, "multiply": calc.multiply, "divide": calc.divide}

    if action not in ops:
        raise ValueError(f"Unknown action: {action}")

    operator = ops[action]
    operands = operands_factory(first_operand, second_operand)
    return operator(operands)
