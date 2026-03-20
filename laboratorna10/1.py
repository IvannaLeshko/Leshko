print("Вміст файлу test1.txt:")
with open("test1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(" ", line.rstrip())
 
symbol = input("\nВведіть символ для пошуку: ")
position = int(input("Введіть позицію (починаючи з 1): "))
 
print(f"\nРядки, де на позиції {position} стоїть символ '{symbol}':")
 
with open("test1.txt", "r", encoding="utf-8") as f:
    found = False
    for line in f:
        line_stripped = line.rstrip("\n")
        if len(line_stripped) >= position:
            if line_stripped[position - 1] == symbol:
                print(" ", line_stripped)
                found = True
 
if not found:
    print("  Таких рядків не знайдено.")
 