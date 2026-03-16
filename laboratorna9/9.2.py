sentence = input("Введіть речення: ")
words = sentence.split() 

all_uppercase = set()

for word in words:
    word_set = set()
    for char in word:
        if 'A' <= char <= 'Z':
            word_set.add(char)
    
    all_uppercase = all_uppercase.union(word_set)

print(f"Об'єднання всіх великих літер зі слів: {all_uppercase}")