matrix = []
with open("matrix_in.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line != "":
            row = []
            for num_str in line.split():
                row.append(int(num_str))
            matrix.append(row)
 
print("Початкова матриця (з файлу matrix_in.txt):")
for row in matrix:
    row_str = ""
    for num in row:
        row_str = row_str + str(num).rjust(5)
    print(row_str)
 
result = []
for i in range(len(matrix)):
    max_elem = matrix[i][0]
    for j in range(1, len(matrix[i])):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
    result.append(max_elem)
    print(f"  Рядок {i + 1}: максимум = {max_elem}")
 
result_matrix = []
for max_elem in result:
    result_matrix.append([max_elem])
 
with open("matrix_out.txt", "w", encoding="utf-8") as f:
    for row in result_matrix:
        row_str = ""
        for i in range(len(row)):
            if i == 0:
                row_str = str(row[i])
            else:
                row_str = row_str + " " + str(row[i])
        f.write(row_str + "\n")
 
print("\nРезультат збережено у файл matrix_out.txt")
print("\nВміст matrix_out.txt (максимум кожного рядка):")
with open("matrix_out.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(f"  Рядок {i + 1}: {line.rstrip()}")