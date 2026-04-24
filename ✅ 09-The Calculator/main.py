from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

cal_dic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_accumulate = True

    num1 = float(input("What is your first number? "))

    while should_accumulate:
        for symbol in cal_dic:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))

        calc_value = cal_dic[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {calc_value}")

        choice = input(f"Type 'y' to continue calculating with {calc_value},"
                       f" or type 'n' to start new calculation. ")

        if choice == "y":
            num1 = calc_value
        else:
            should_accumulate = False
            print("\n" * 20)
            break

calculator()
