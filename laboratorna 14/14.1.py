class Product:
    STORAGE_RATE = 0.0013

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def storage_cost(self):
        return self.quantity * self.price * self.STORAGE_RATE

    def __str__(self):
        return (
            f"Товар: '{self.name}', кількість: {self.quantity} од., "
            f"ціна: {self.price} грн\n"
            f"  Вартість товару:     {self.total_value():.2f} грн\n"
            f"  Вартість зберігання: {self.storage_cost():.2f} грн"
        )


if __name__ == "__main__":
    p1 = Product("Цукор", 200, 45.00)
    p2 = Product("Борошно", 500, 32.50)

    print(p1)
    print()
    print(p2)