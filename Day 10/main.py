import art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print(art.logo)
    first_number = float(input("What is the first number?\n"))

    while True:
        operation = input("Pick the operation: +, -, *, /\n")
        next_number = float(input("What is the next number?\n"))
        answer = operations[operation](first_number,next_number)
        print(f"{first_number} {operation} {next_number} = {answer}" )

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            first_number = answer
        else:
            os.system("cls")
            calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculator()