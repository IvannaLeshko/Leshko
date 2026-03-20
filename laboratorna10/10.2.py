print("Вміст файлу test2.txt:")
with open("test2.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(" ", line.rstrip())
 
minimum = None
 
with open("test2.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line != "":
            number = int(line)
            if minimum is None:
                minimum = number
            elif number < minimum:
                minimum = number
 
print(f"\nМінімальне число: {minimum}")