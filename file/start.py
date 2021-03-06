from .work.read import reading, searching
from .work.write import creating, editing, deleting, updating_t, updating_o
from .classes.Tovar import Tovar
from .classes.Order import Order
from .startui import uistart

from .UIview import uivie


def start():
    print("\nВас вітає АРМ комп'ютерного магазину {НеСмАк}")
    print("\nДоступні функції:"
          "\n1 -- Перегляд товару"
          "\n2 -- Додавання нового товару"
          "\n3 -- Видалення товару"
          "\n4 -- Змінити ціну"
          "\n5 -- Поставте."
          "\n6 -- Оформити замовлення"
          "\n7 -- Пошук по назві товару"
          "\n8 -- Тестовий перепис"
          "\n9 -- Тестовий запуск UI"
          "\n10 - вихід з програми\n")
    try:
        choice = int(input())
    except:
        return 0
    if choice == 1:
        reading()
    elif choice == 2:
        updating_t(Tovar(input(), input(), input()))
        print("Товар успішно додано!")
    elif choice == 3:
        deleting(input())
    elif choice == 4:
        editing(input())
    elif choice == 5:
        print("Поставте. Саме так")
    elif choice == 6:
        updating_o(Order(input(), input()))
    elif choice == 7:
        searching(input())
    elif choice == 8:
        creating()
        updating_t(Tovar('RTX 3080', 129999, 22))
        updating_t(Tovar('RTX 3070', 109999, 30))
        updating_t(Tovar('RX 6900XT', 109998, 34))
        updating_o(Order(5, "20.12.2020"))
        updating_o(Order(1, "25.11.2021"))
    elif choice == 9:
        uivie()
    elif choice == 10:
        from sys import exit
        exit(0)
    else:
        print("Анука малєнько краще по клаві прошарились, а")
        start()
