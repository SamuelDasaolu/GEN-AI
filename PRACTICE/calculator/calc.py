def give_error(message):
    print(f"An error occurred: {message}")


def check_denominator(num):
    if num == 0 or num == '0':
        raise ZeroDivisionError


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    check_denominator(b)
    return a / b


def modulo(a, b):
    check_denominator(b)
    return a % b


def exponent(a, b):
    return a ** b


