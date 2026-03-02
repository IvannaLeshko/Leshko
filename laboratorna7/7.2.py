import random

name = "Ivanna"      
surname = "Leshko" 

n, m = len(name), len(surname)

matrix = [[random.random() for _ in range(n)] for _ in range(m)]

print("Матриця:")
for row in matrix:
    print([round(x, 2) for x in row])


column_sums = [0] * n
for row in matrix:
    for i in range(n):
        column_sums[i] += row[i]

print("\nСуми стовпчиків:")
print([round(s, 2) for s in column_sums])