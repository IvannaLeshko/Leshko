import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

print(" x      y")

while x <= b:

    if 16 - x*x != 0 and x + 3 >= 0:

        y = 1 / (16 - x*x) + math.sqrt(x + 3)

        print(round(x, 2), " ", round(y, 5))

    else:
        print(round(x, 2), "  немає значення")

    x = x + h
