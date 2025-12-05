# main.py
# Точка входа — консольное меню для информационной системы "Цветочный магазин"
"""
Примечание:
    В рамках лабораторной работы №3 я планирую сделать перенос системы с консольного приложения на веб-интерфейс.
    Для реализации будет использоваться фреймворк Flask или аналогичный инструмент.
"""

# Это тестовое изменение для ветки dev

# Это ещё одно тестовое изменение для ветки div

# TODO: Финальное тестовое изменение для push из 5 задания!

from catalog import show_catalog
from cart import Cart
from order import create_order
from user import login_user
from database import Database


def main():
    db = Database()
    cart = Cart(db)

    print("Добро пожаловать в информационную систему 'Цветочный магазин'!\n")

    user = login_user()

    while True:
        print("1. Просмотреть каталог")
        print("2. Просмотреть корзину")
        print("3. Добавить товар в корзину")
        print("4. Удалить товар из корзины")
        print("5. Оформить заказ")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_catalog(db)
            print("========================")
        elif choice == "2":
            cart.view_cart()
            print("========================")
        elif choice == "3":
            cart.add_to_cart()
            print("========================")
        elif choice == "4":
            cart.remove_from_cart()
            print("========================")
        elif choice == "5":
            create_order(user, cart, db)
            print("========================")
        elif choice == "6":
            print("Спасибо за использование системы! До свидания.")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
