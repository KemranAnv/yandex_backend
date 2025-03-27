import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {}


def add(items, title, amount, expiration_date=None):

    try:
        expiration_date = datetime.datetime.strptime(expiration_date,
                                                     DATE_FORMAT).date()
    except TypeError:
        pass

    if title in items:
        items[title].append({'amount': amount,
                             'expiration_date': expiration_date})
    elif title not in items:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]


add(goods, 'Яйца', Decimal('10'), '2023-09-30')
add(goods, 'Пельмени Универсальные', Decimal('0.5'), '2023-07-15')
add(goods, 'Пельмени Универсальные', Decimal('2'), '2023-08-01')


def add_by_note(items, note):
    parts = note.split()
    expiration_date = None
    try:
        expiration_date = datetime.datetime.strptime(parts[-1],
                                                     DATE_FORMAT).date()
    except ValueError:
        pass

    if expiration_date:
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    elif not expiration_date:
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
add_by_note(goods, 'Вода 2.5')


def find(items, needle):
    result = []
    needle_lower = needle.lower()

    for title in items:
        if needle_lower in title.lower():
            list.append(result, title)

    return result


goods = {
    'Яйца': [{'amount': Decimal('1'),
              'expiration_date': datetime.date(2023, 6, 24)}],
    'Яйца гусиные': [{'amount': Decimal('4'),
                      'expiration_date': datetime.date(2023, 7, 15)}],
    'Морковь': [{'amount': Decimal('2'),
                 'expiration_date': datetime.date(2023, 8, 6)}]
}

# print(find(goods, 'йц'))  # Регистр не имеет значения


def amount(items, needle):
    total_amount = Decimal('0')

    for title in find(items, needle):
        total_amount += sum(item['amount'] for item in items[title])

    return total_amount


# Пример использования:
goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
    'Морковь': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
    ],
    'Вода': [{'amount': Decimal('2.5'), 'expiration_date': None}]
}

# print(amount(goods, 'яйца'))  # 1
# print(amount(goods, 'морковь'))  #


def expire(items, in_advance_days=0):
    now = datetime.date.today()
    check_date = now + datetime.timedelta(days=in_advance_days)

    expired = []

    for title, batches in items.items():
        total_amount = Decimal('0')
        for batch in batches:
            if (batch['expiration_date'] and
               batch['expiration_date'] <= check_date):
                total_amount += batch['amount']
        if total_amount > 0:
            expired.append((title, total_amount))

    return expired


# Пример использования:
goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 12, 9)}
    ],
    'Яйца': [
        {'amount': Decimal(
            '2'), 'expiration_date': datetime.date(2023, 12, 12)},
        {'amount': Decimal(
            '3'), 'expiration_date': datetime.date(2023, 12, 11)}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}

print(expire(goods))  # Продукты, чьи сроки истекли
