def calculator(number1, number2, operator):
    if not isinstance(number1, (float, int)):
        return False
    if not isinstance(number2, (float, int)):
        return False
    if operator == "+":
            return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "//":
        return number1 // number2
    elif operator == "**":
        return number1 ** number2
    else:
        return False

def parse_input():
    text = input("Enter equation: ")
    list = text.split()
    num1 = float(list[0])
    oper = list[1]
    num2 = float(list[2])
    print(calculator(num1, num2, oper))
