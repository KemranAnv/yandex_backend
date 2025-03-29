# Импортируйте необходимые модули.
import datetime


DATE_FORMAT = '%d.%m.%Y'


# Укажите два параметра функции:
def validate_record(name, date_of_birth):
    # Напишите код, верните булево значение.
    try:
        datetime.datetime.strptime(date_of_birth, DATE_FORMAT)
    except ValueError:
        print('Некорректный формат даты в записи: '
              f'{name}, {date_of_birth}')
        return False
    else:
        return True


# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0

    dict_of_count = {'good': 0, 'bad': 0}

    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.
    for item in data:
        key, value = item
        check = validate_record(key, value)
        if check:
            good_count += 1
        elif not check:
            bad_count += 1

    dict_of_count['good'] = good_count
    dict_of_count['bad'] = bad_count

    return dict_of_count


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]

statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>

correct = statistics['good']
incorrect = statistics['bad']

print(f'Корректных записей: {correct}')
print(f'Некорректных записей: {incorrect}')
