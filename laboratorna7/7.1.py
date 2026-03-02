import random

try:
    n = int(input("Введіть кількість елементів n: "))
except ValueError:
    print("Будь ласка, введіть ціле число.")
    exit()

list_a = [random.random() for _ in range(n)]

list_b = [random.randint(-10, 10) for _ in range(n)]

list_c = [random.randint(0, 50) for _ in range(n)]

print(f"\nСписок (а) [0, 1]: {list_a[:5]}... (показано перші 5)")
print(f"Список (б) [-10, 10]: {list_b}")
print(f"Список (в) [0, 50]: {list_c}")

sum_abs = 0
found_zero = False
zero_index = -1

for i in range(len(list_b)):
    if list_b[i] == 0:
        found_zero = True
        zero_index = i
        for j in range(i + 1, len(list_b)):
            sum_abs += abs(list_b[j])
        break

print("\n--- Результат для списку (б) ---")
if found_zero:
    print(f"Перший нуль знайдено на позиції (індексі): {zero_index}")
    print(f"Сума модулів елементів після нього: {sum_abs}")
else:
    print("У списку (б) немає нульових елементів.")