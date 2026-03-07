text = input("Введіть текст з повторами: ")
words = text.split()
unique_words = set(words)

for word in unique_words:
    print(word)