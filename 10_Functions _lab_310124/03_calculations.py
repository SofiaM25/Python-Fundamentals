operator = input()
number1 = int(input())
number2 = int(input())


def calculate_data(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 / num2
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


result = calculate_data(operator, number1, number2)
print(int(result))

