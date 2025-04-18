# Задание 2

В торговой сети ООП есть три вида магазинов:

* мини-маркеты — работают только по будним дням,
* магазины выходного дня — работают только по субботам и воскресеньям,
* non-stop маркеты — эти магазины работают ежедневно.

Напишите программу, с помощью которой пользователи смогут узнать, работает ли в заданную дату тот или иной магазин.

## В коде описаны

* родительский класс `Store`, описывающий «магазин в общем»; в этом классе
    -> атрибут `address` принимает адрес магазина;
    -> метод `get_info()` принимает на вход строку с датой в формате `ДД.ММ.ГГГГ` и возвращает информацию, открыт ли магазин в указанный день;
    -> метод `is_open()` принимает на вход объект даты; это метод-заглушка, его нужно переопределить в дочерних классах;
* три класса-наследника: `MiniStore`, `WeekendStore` и `NonStopStore`.

## Ваша задача

* допишите метод `get_info()` в родительском классе `Store` так, чтобы этот метод возвращал информацию о том, работает ли конкретный магазин в указанный день;
* в дочерних классах `MiniStore`, `WeekendStore` и `NonStopStore` переопределите метод `is_open()` так, чтобы он возвращал `True` в том случае, если в указанную дату магазин работает.

## Например

Для даты `30.03.2024` (это суббота) метод `is_open()` в дочерних классах должен работать так:

* Если эту дату передать в метод `is_open()` класса `MiniStore` — метод должен вернуть `False` (по выходным минимаркеты не работают).
* Если эту дату передать в метод `is_open()` класса `WeekendStore` — метод должен вернуть `True` (магазины выходного дня работают по субботам и воскресеньям).
* Если эту дату передать в метод `is_open()` класса `NonStopStore` — метод должен вернуть `True` (такие магазины работают вообще всегда, в любой день).
