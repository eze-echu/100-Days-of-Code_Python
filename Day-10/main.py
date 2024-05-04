from art import logo


operations = ["add", "subtract", "multiply", "divide", "power", "root",
              'a', 's', 'm', 'd', 'p', 'r',
              '+', '-', '*', '/', '**', '/*']

def add(n1: float | int, n2: float | int) -> float | int | None:
    try:
        if type(n1) is float | int and type(n2) is float | int:
            return n1 + n2
        else:
            raise TypeError
    except TypeError:
        print("Only numbers allowed")
        return None


def subtract(n1: float | int, n2: float | int) -> float | int | None:
    try:
        if type(n1) is float | int and type(n2) is float | int:
            return n1 - n2
        else:
            raise TypeError
    except TypeError:
        print("Only numbers allowed")
        return None


def multiply(n1: float | int, n2: float | int) -> float | int | None:
    try:
        if type(n1) is float | int and type(n2) is float | int:
            return n1 * n2
        else:
            raise TypeError
    except TypeError:
        print("Only numbers allowed")
        return None


def divide(n1: float | int, n2: float | int) -> float | int | None:
    try:
        if type(n1) is float | int and type(n2) is float | int:
            return n1 / n2
        else:
            raise TypeError
    except TypeError:
        print("Only numbers allowed")
        return None


def power(n1: float | int, n2: float | int) -> float | int | None:
    try:
        if type(n1) is float | int and type(n2) is float | int:
            return n1 ** n2
        else:
            raise TypeError
    except TypeError:
        print("Only numbers allowed")
        return None


def square(n1: float | int, n2: float | int) -> float | int | None:
    try:
        if type(n1) is float | int and type(n2) is float | int:
            return n1 ** (1.00 / n2)
        else:
            raise TypeError
    except TypeError:
        print("Only numbers allowed")
        return None


def operate(n1: float | int, n2: float | int, operation: str) -> float | int | None:
    try:
        if isinstance(n1, (float, int)) and isinstance(n2, (float, int)):
            if operation in operations:
                match operation:
                    case "add" | "a" | "+":
                        return n1 + n2
                    case "subtract" | "s" | "-":
                        return n1 - n2
                    case "multiply" | "m" | "*":
                        return n1 * n2
                    case "divide" | "d" | "/":
                        return n1 / n2
                    case "power" | "p" | "**":
                        return n1 ** n2
                    case "root" | "r" | "/*":
                        return n1 ** 1/n2
                    case _:
                        raise ValueError
            else:
                raise ValueError
        else:
            return operate(float(n1), float(n2), operation)
    except TypeError:
        print("Only numbers allowed")
    except ValueError:
        print("Value Error Raised")
    return None


if __name__ == "__main__":
    print(logo)
    use_ans = False
    ans = float()
    while True:
        if use_ans:
            num1 = ans
            print(f"Type first number: \n{num1}")
        else:
            num1 = input("Type first number: \n")
        operator = input("What operation would you like to do? \n"
                         "Add +\n"
                         "Subtract -\n"
                         "Multiply *\n"
                         "Divide /\n"
                         "Power ** \n"
                         "Square /* \n")
        num2 = input("Type second number: \n")
        ans = operate(n1=num1, n2=num2, operation=operator)
        if ans is not None:
            print(f"{num1} {operator} {num2} = {ans}")
        redo = input("Would you like to make another calculation (y/n)? \n")
        if redo == "y":
            if ans is not None:
                reuse = input("Would you like to use the previous answer (y/n)?")
                if reuse == "y":
                    use_ans = True
                else:
                    use_ans = False
            else:
                use_ans = False
        else:
            break
