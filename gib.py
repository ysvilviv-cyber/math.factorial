import math
radius = int(input("Ведіть радіус кола: "))
def calculator():
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi*(radius**2)

print(f"Площа кола: {calculator()}")