# database.py
# Эмуляция базы данных для информационной системы "Цветочный магазин"

class Database:
    def __init__(self):
        # Каталог товаров
        self.products = [
            {"name": "Букет из роз", "price": 1500, "stock": 10},
            {"name": "Букет из Орхидей", "price": 2200, "stock": 8},
            {"name": "Букет из гипсофил", "price": 900, "stock": 12},
            {"name": "Тюльпаны", "price": 950, "stock": 3},
            {"name": "Ромашки", "price": 700, "stock": 20},
        ]

        # Список заказов
        self.orders = []

        # Список пользователей (упрощённо)
        self.users = [
            {"name": "admin", "role": "admin"},
            {"name": "гость", "role": "customer"}
        ]

    def get_products(self):
        """Возвращает список всех товаров."""
        return self.products

    def get_product(self, name):
        """Поиск товара по названию."""
        for product in self.products:
            if product["name"].lower() == name.lower():
                return product
        return None

    def add_order(self, order):
        """Добавляет заказ в список заказов."""
        self.orders.append(order)

    def list_orders(self):
        """Возвращает все заказы."""
        return self.orders
