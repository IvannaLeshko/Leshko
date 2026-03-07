text = input("Введіть речення: ")
words = text.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)
print(result)