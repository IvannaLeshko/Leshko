N = int(input("Введіть N (2 ≤ N < 99): "))

for i in range(N):

    if i % 2 == 0:  
        for j in range(N):
            print(i + j + 2, end=" ")
    else:         
        for j in range(N):
            print(0, end=" ")

    print() 
