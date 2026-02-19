str_info = "Іванна КН-3 Комп'ютерні науки"

parts = str_info.split()
group = parts[1]
print(f"Група: {group}")

new_str = str_info.replace("Іванна", "Лешко")
print(new_str)

words = str_info.split(" ")
print(f"Кількість слів: {len(words)}")