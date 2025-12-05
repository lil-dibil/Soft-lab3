# order.py
# Оформление заказа для системы "Цветочный магазин"

# Это тестовое изменение для ветки dev
def create_order(user, cart, db):
    """Создание заказа на основе содержимого корзины."""
    if not cart.items:
        print("\nВаша корзина пуста. Добавьте товары перед оформлением заказа.")
        return

    name = user.get("name", "Неизвестный клиент")

    # Подсчёт суммы с учётом количества
    total = sum(item["product"]["price"] * item["quantity"] for item in cart.items)

    # Формируем данные заказа
    order_data = {
        "customer": name,
        "items": [
            {
                "name": item["product"]["name"],
                "quantity": item["quantity"],
                "price": item["product"]["price"]
            }
            for item in cart.items
        ],
        "total": total
    }

    db.add_order(order_data)

    # Красивый вывод чека
    print("\nЗаказ успешно оформлен!")
    print(f"Покупатель: {name}")
    print("Состав заказа:")
    for item in order_data["items"]:
        print(f" - {item['name']} x {item['quantity']} = {item['price'] * item['quantity']} руб.")
    print(f"Итого к оплате: {total} руб.\n")

    # После оформления очищаем корзину
    cart.items.clear()
