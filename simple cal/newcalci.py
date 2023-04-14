operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "//": lambda x, y: x//y,
    "**": lambda x, y: x ** y,
    "%": lambda x, y: x % y
}

def calci():

    a = int(input("Enter first number : "))

    b = int(input("Enter second second : "))

    print("enter what do you want to performe out of this")

    operation = input(list(operations.keys()))

    function = operations.get(operation)

    if (function):
        print("Result: ", function(a, b))
    else:
        print("enter valid input")

calci()
