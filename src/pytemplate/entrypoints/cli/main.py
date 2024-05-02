from argparse import ArgumentParser, Namespace
from typing import Tuple, Union

from src.pytemplate.service.calculator import Calculator
from src.pytemplate.domain.models import Operands


parser = ArgumentParser()
parser.add_argument('-f',"--first_operand", type=int, 
                    help="First operand", required=False)

parser.add_argument('-s',"--second_operand", type=int, 
                    help="Second operand", required=False)

parser.add_argument('-o',"--operation", type=str, 
                    help="Operation", required=False, 
                    choices=["add", "subtract", "multiply", "divide"])

parser.add_argument('-i', '--interactive', action='store_true', 
                    help='Run the program in interactive mode',
                    default=False)

args = parser.parse_args()


def calc_interactive() -> Tuple[Operands, str]:
    valid_ops = ["add", "subtract", "multiply", "divide"]
    first_operand = int(input("First operand: "))
    second_operand = int(input("Second operand: "))
    while True:
        operation = input(f"Operation [{valid_ops}]: ")
        if operation not in valid_ops:
            print("Invalid operation, try again or Ctrl+C to exit")
        else:
            break
    
    return Operands(first_operand, second_operand), operation


def main()->Union[int, None]:
    calculator = Calculator()
    ops = {'add': calculator.add, 
               'subtract': calculator.subtract, 
               'multiply': calculator.multiply, 
               'divide': calculator.divide}
    
    if args.interactive is True:
        operands, operation = calc_interactive()
    
    elif args.first_operand and args.second_operand and args.operation:
        operands = Operands(args.first_operand, args.second_operand)
        operation = args.operation
    else:
        raise ValueError("Missing operand or operation, try --help for more info")

    calc_result = ops[operation](operands)
    print(calc_result)
    input("Press any key to exit...")
    return calc_result


if __name__ == "__main__":
    main()
