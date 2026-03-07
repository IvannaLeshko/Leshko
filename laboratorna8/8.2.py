text = input("Введіть рядок: ")
words = text.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)