# Импортируйте нужную библиотеку.
from datetime import datetime


class Store:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        # Метод is_open() в родительском классе всегда возвращает False,
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        return False

    def get_info(self, date_str):
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(date_str, '%d.%m.%Y').date()

        # Передайте в метод is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class MiniStore(Store):
    # Переопределите метод is_open().
    def is_open(self, date):
        week_name = date.weekday()
        if 0 <= week_name <= 4:
            return True
        elif week_name > 4:
            return False


class WeekendStore(Store):
    # Переопределите метод is_open().
    def is_open(self, date):
        week_name = date.weekday()
        if 5 <= week_name <= 6:
            return True
        elif week_name < 5:
            return False


class NonStopStore(Store):
    # Переопределите метод is_open().
    def is_open(self, date):
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))
