# Задание 1

##

С середины восемнадцатого века и по сей день данные о сотрудниках компании «Артель Свѣтлое будущее» традиционно хранят в амбарных книгах.

Каждая страница книги поделена на два столбца: в левом указаны имя и фамилия сотрудника, а в правом — дата рождения:

1. Акакій Башмачкинъ   -   23 марта 1791 года
2. Яков Степанов       -   Двадцать шестое июля 1971
3. Потап Алексеев      -  16.09.1990
4. Евгений Женин       -   5 декабря 1984
5. Кондрат Александров - 18.01.1994

Но прогресс не стоит на месте: список пришлось оцифровать.

При оцифровке предполагалось, что даты будут в формате `ДД.ММ.ГГГГ`, однако при заполнении книг не все писари, клерки и менеджеры соблюдали этот формат и писали даты как попало.

Напишите программу, которая получит на вход такой список кортежей с данными:

```python
data = [
    ('Акакій Башмачкинъ',    '23 марта 1791 года'),
    ('Яков Степанов', 'Двадцать шестое июля 1971'),
    ('Потап Алексеев', '16.09.1990'),
    ('Евгений Женин', '5 декабря 1984'),
    ('Кондрат Александров', '18.01.1994')
] 
```

### Программа должна подсчитать

* количество записей, где дата указана корректно;
* количество записей, где дата указана некорректно

### и вывести на экран

* все записи с некорректным форматом даты;
* количество записей, где дата указана корректно;
* количество записей, где дата указана некорректно.

В ходе обработки данных из списка программа должна вывести такой результат:

```python
Некорректный формат даты в записи: Акакій Башмачкинъ, 23 марта 1791 года
Некорректный формат даты в записи: Яков Степанов, Двадцать шестое июля 1971
Некорректный формат даты в записи: Евгений Женин, 5 декабря 1984
Корректных записей: 2
Некорректных записей: 3 
```

## В программе должны быть две функции

### 1

Функция `process_people()` должна принять на вход список кортежей `data`,в каждом из которых первый элемент — имя, а второй — дата рождения.

В функции должны быть объявлены два счетчика:

* `good_count` для подсчёта корректных записей;
* `bad_count` для подсчёта некорректных записей.

В каждом кортеже из списка `data` надо проверить, в правильном ли формате указана дата рождения сотрудника. Для этой проверки должна вызываться функция `validate_record()`. В результате проверки должно увеличиться значение одного из счётчиков.

В конце функция должна вернуть словарь с ключами `good` и `bad`, где значениями будут значения счётчиков `good_count` и `bad_count`.

### 2

Функция `validate_record()` должна принимать на вход два аргумента: имя сотрудника и дату его рождения.

С помощью метода `datetime.strptime()` проверьте, соответствует ли полученная строка с датой рождения формату `ДД.ММ.ГГГГ`.

В случае, если строка не соответствует ожидаемому формату — метод `datetime.strptime()` выбросит исключение. Обработайте это исключение:

* напечатайте сообщение

    ```python
    Некорректный формат даты в записи: <имя>, <дата_рождения>
    ```

* верните из функции `False`.

Если дата рождения соответствует ожидаемому формату — верните `True`.
