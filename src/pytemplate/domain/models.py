from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

def operands_factory(first_operand: int, second_operand: int) -> Operands:
    """ builds operands based on the input couple of values """
    return Operands(first_operand, second_operand)