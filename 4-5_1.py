N = int(input("Введіть N: "))

dob = 1

for i in range(1, N + 1):
    chys = 2 * i
    znam = 2 * i * i + 1
    dob = dob * (chys / znam)

print("Добуток =", dob)
