import math

def calculate_square_root(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return None

numero = float(input("Enter a number: "))

squareRoot = calculate_square_root(numero)

if squareRoot is not None:
    print(f"The square root of {numero} is {squareRoot}")
else:
    print("The square root of a negative number cannot be calculated.")