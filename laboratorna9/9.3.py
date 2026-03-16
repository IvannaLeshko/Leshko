
travel_vouchers = []

count = int(input("Скільки путівок додати до списку? "))

for i in range(count):
    print(f"\n--- Введення путівки №{i+1} ---")
    
    voucher = {
        "місяць": input("Місяць відпочинку: "),
        "місце": input("Місце відпочинку: "),
        "зірки": int(input("Кількість зірок (1-4): ")),
        "кількість_туристів": int(input("Кількість туристів: ")),
        "вартість_1_особа": float(input("Вартість за 1-го туриста ($): "))
    }
    
    travel_vouchers.append(voucher)
print("\nВаш список путівок:")
for v in travel_vouchers:
    print(v)