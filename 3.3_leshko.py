years_lived = int(input("Введіть кількість прожитих років: "))

if years_lived < 6:
    print("Ще не школяр")
elif 6 <= years_lived <= 9:
    print("Початкова школа")
elif 10 <= years_lived <= 15:
    print("Середня школа")
elif 16 <= years_lived <= 17:
    print("Старша школа")
else:
    print("Вже не школяр")
