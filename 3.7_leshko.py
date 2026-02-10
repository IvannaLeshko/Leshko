temperature = int(input("Введіть температуру: "))

if temperature < 10:
    print("Холодно")
elif 10 <= temperature <= 25:
    print("Тепло")
else:
    print("Спекотно")
