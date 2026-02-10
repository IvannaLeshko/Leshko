length_x = float(input("Введіть довжину першої сторони трикутника: "))
length_y = float(input("Введіть довжину другої сторони трикутника: "))
length_z = float(input("Введіть довжину третьої сторони трикутника: "))

if length_x + length_y > length_z and length_x + length_z > length_y and length_y + length_z > length_x:
    if length_x == length_y == length_z:
        print("Рівносторонній трикутник")
    elif length_x == length_y or length_x == length_z or length_y == length_z:
        print("Рівнобедрений трикутник")
    else:
        print("Різносторонній трикутник")
else:
    print("Трикутник не існує")
