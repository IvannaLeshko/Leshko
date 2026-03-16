
vouchers_with_transport = []

n = int(input("Введіть кількість путівок: "))

for i in range(n):
    print(f"\n--- Дані про тур №{i+1} ---")
    
    month = input("Місяць: ")
    destination = input("Куди їдемо: ")
    hotel_stars = int(input("Зірок у готелі (1-4): "))
    tourists = int(input("Кількість людей: "))
    price = float(input("Ціна за одного ($): "))
    
    t_name = input("Транспорт: ")
    t_food = input("Харчування (так/ні): ")
    t_time = float(input("Час у дорозі (год): "))
    
    transport_info = {
        "назва": t_name,
        "харчування": t_food,
        "час_в_дорозі": t_time
    }
    
    final_voucher = {
        "місяць": month,
        "місце": destination,
        "зірки": hotel_stars,
        "туристи": tourists,
        "ціна": price,
        "транспорт": transport_info  
    }
    
    vouchers_with_transport.append(final_voucher)

print("\n--- Зареєстровані путівки ---")
for v in vouchers_with_transport:
    print(f"Місце: {v['місце']} | Транспорт: {v['транспорт']['назва']} | Час у дорозі: {v['транспорт']['час_в_дорозі']} год.")