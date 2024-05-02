from src.pytemplate.domain.models import Operands


class Calculator:
    def add(self, operands: Operands):
        return operands.first_operand + operands.second_operand

    def subtract(self, operands: Operands):
        return operands.first_operand - operands.second_operand

    def multiply(self, operands: Operands):
        return operands.first_operand * operands.second_operand

    def divide(self, operands: Operands):
        if operands.second_operand == 0:
            raise ZeroDivisionError("What are you trying to do...")
        
        return operands.first_operand / operands.second_operand 