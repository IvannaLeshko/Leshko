eps = float(input("Введіть ε: "))

suma = 0
i = 1

while True:

    dodatok = ((-1) ** i) / i
    suma = suma + dodatok

    if abs(dodatok) < eps:
        break

    i = i + 1

print("Сума =", suma)
print("Кількість членів =", i)
