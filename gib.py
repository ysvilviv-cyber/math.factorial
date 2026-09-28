import math
def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        return (x1, x2)
    elif D == 0:
        x = -b/(2*a)
        print(f"Один корінь: {x}")
    else:
        print("Немає дійсних коренів дискрімінант відємний")

# Рівняння x² - 5x + 6 = 0 (D > 0)
print(solve_quadratic(1, -5, 6))   # Виведе: (3.0, 2.0)

# Рівняння x² - 4x + 4 = 0 (D = 0)
print(solve_quadratic(1, -4, 4))   # Виведе: 2.0

# Рівняння x² + 4x + 5 = 0 (D < 0)
print(solve_quadratic(1, 4, 5))    # Виведе: Немає дійсних коренів
