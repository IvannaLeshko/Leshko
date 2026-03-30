import math


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less    = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
 

def search_by_value(lst, value):
    indices = [i for i, x in enumerate(lst) if x == value]
    return indices if indices else -1

def first_five_min(lst):
    result = []
    temp = lst[:]
    for _ in range(min(5, len(temp))):
        m = min(temp)
        result.append(m)
        temp.remove(m)
    return result
 
def arithmetic_mean(lst):
    if not lst:
        return None
    total = 0
    for x in lst:
        total += x
    return total / len(lst)
 
def remove_duplicates(lst):
    seen = {}
    for x in lst:
        seen[x] = True
    return list(seen.keys())
 
data = [12, 4, 7, 4, 1, 15, 3, 7, 9, 1, 6, 15, 2, 8, 3]
print(f"Початковий список    : {data}")
print(f"Відсортований список : {quick_sort(data)}")
print(f"Пошук числа 7        : індекси {search_by_value(data, 7)}")
print(f"Пошук числа 99       : {search_by_value(data, 99)}")
print(f"5 мінімальних        : {first_five_min(data)}")
print(f"Середнє арифметичне  : {arithmetic_mean(data):.4f}")
print(f"Без повторів         : {remove_duplicates(data)}")