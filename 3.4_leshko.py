brace = input("Введіть символ-дужку: ")

if brace == "(" or brace == ")":
    print("Кругла дужка")
elif brace == "[" or brace == "]":
    print("Квадратна дужка")
elif brace == "{" or brace == "}":
    print("Фігурна дужка")
else:
    print("Невідомий символ")
