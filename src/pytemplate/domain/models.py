from dataclasses import dataclass


@dataclass
class Operands:
    """sci operands"""

    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    """factory for operands"""

    return Operands(first_operand, second_operand)
