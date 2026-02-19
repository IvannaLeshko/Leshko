numbers = [10, 20, 30, 40, 50, 60]
numbers.insert(1, -5)
min_val = min(numbers)
max_val = max(numbers)
numbers[2:2] = [1, 2, 3]
numbers.append("Лешко Іванна")
count_elements = len(numbers)

print(numbers)
print(f"Min: {min_val}, Max: {max_val}")
print(f"Кількість: {count_elements}")