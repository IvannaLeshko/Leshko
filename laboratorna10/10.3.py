print("Вміст файлу test3.txt:")
with open("test3.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(" ", line.rstrip())
 
n = int(input("\nВведіть кількість символів N для порівняння: "))
 
with open("test3.txt", "r", encoding="utf-8") as f_in:
    with open("result3.txt", "w", encoding="utf-8") as f_out:
        count = 0
        for line in f_in:
            line_stripped = line.rstrip("\n")
            if len(line_stripped) >= 2 * n:
                first_n = line_stripped[:n]
                last_n = line_stripped[-n:]
                if first_n == last_n:
                    f_out.write(line_stripped + "\n")
                    count += 1
 
print(f"\nЗнайдено {count} рядків. Результат збережено у файл result3.txt")
print("\nВміст result3.txt:")
with open("result3.txt", "r", encoding="utf-8") as f:
    content = f.read()
    if content.strip() == "":
        print("  (файл порожній - таких рядків не знайдено)")
    else:
        for line in content.splitlines():
            print(" ", line)