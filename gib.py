import math
def gipotinuza_tricutnic(a,b,c):
## a --- катет
## b --- катет
## c --- гіпотинуза
    c = math.sqrt(a**2 + b**2)

    print(f"Гіпотинуза дорівнює: {c}")
gipotinuza_tricutnic(3,6, 0)
