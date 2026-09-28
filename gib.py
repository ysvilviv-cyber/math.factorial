import math
factorial = int(input("Ведіть ваш факторіал: "))
def factorial_action(n):
    if factorial < 0:
        raise ValueError("Ваше число відємне")
    return math.factorial(factorial)
print(factorial_action(factorial))
