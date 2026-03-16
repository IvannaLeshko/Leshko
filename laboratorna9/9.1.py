line1 = input("Введіть перший рядок: ")
line2 = input("Введіть другий рядок: ")

s1 = set()
for char in line1:
    if 'A' <= char <= 'Z':
        s1.add(char)

s2 = set()
for char in line2:
    if 'A' <= char <= 'Z':
        s2.add(char)

intersection = s1.intersection(s2)

print(f"Множина S1: {s1}")
print(f"Множина S2: {s2}")
print(f"Перетин (спільні літери): {intersection}")