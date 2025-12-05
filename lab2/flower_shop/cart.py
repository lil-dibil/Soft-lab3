# cart.py
# Модуль корзины для системы "Цветочный магазин"

class Cart:
    def __init__(self, db):
        self.items = []      # Список словарей: {"product": {...}, "quantity": n}
        self.db = db         # Ссылка на базу данных

    def add_to_cart(self):
        """Добавляет товар в корзину по номеру из каталога."""
        products = self.db.get_products()

        # Выводим каталог
        print("\n=== КАТАЛОГ ТОВАРОВ ===")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product['name']} — {product['price']} руб. (в наличии: {product['stock']})")

        try:
            index = int(input("\nВведите номер товара для добавления: "))
            if index < 1 or index > len(products):
                print("Ошибка: Неверный номер товара.")
                return
        except ValueError:
            print("Ошибка: Введите корректное число.")
            return

        product = products[index - 1]

        try:
            qty = int(input(f"Введите, сколько '{product['name']}' добавить в корзину: "))
        except ValueError:
            print("Ошибка: Введите корректное число.")
            return

        if qty <= 0:
            print("️Ошибка: Количество должно быть больше нуля.")
            return
        if qty > product["stock"]:
            print(f"Недостаточно товара на складе. В наличии: {product['stock']} шт.")
            return

        # Проверяем, есть ли этот товар уже в корзине
        for item in self.items:
            if item["product"]["name"].lower() == product["name"].lower():
                item["quantity"] += qty
                break
        else:
            self.items.append({"product": product, "quantity": qty})

        product["stock"] -= qty
        print(f"{product['name']} ({qty} шт.) добавлен(ы) в корзину.")

    def view_cart(self):
        """Показывает содержимое корзины."""
        if not self.items:
            print("\nВаша корзина пуста.")
            return

        print("\n=== ВАША КОРЗИНА ===")
        total = 0
        for i, item in enumerate(self.items, 1):
            product = item["product"]
            subtotal = product["price"] * item["quantity"]
            total += subtotal
            print(f"{i}. {product['name']} — {product['price']} руб. x {item['quantity']} = {subtotal} руб.")
        print(f"----------------------\nИтого: {total} руб.\n")

    def remove_from_cart(self):
        """Удаляет товар из корзины по номеру."""
        if not self.items:
            print("\nВаша корзина пуста.")
            return

        self.view_cart()
        try:
            index = int(input("Введите номер товара для удаления: "))
            if index < 1 or index > len(self.items):
                print("Ошибка: Неверный номер товара.")
                return
        except ValueError:
            print("️Ошибка: Введите корректное число.")
            return

        removed_item = self.items.pop(index - 1)
        # Возвращаем удалённое количество обратно на склад
        removed_item["product"]["stock"] += removed_item["quantity"]
        print(f"Товар '{removed_item['product']['name']}' удалён из корзины.")