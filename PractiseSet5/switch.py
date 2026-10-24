num1 = 10
num2 = 5

operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)

    case "/":
        print(num1 / num2)

    case _:
        print("Invalid operator")