# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.
# comprehension_numbers = (digit ** 2 for digit in numbers if (digit % 3 == 0))
comprehension_numbers_2 = (digit ** 2 for digit in numbers if (digit % 3 == 0))

# Распечатайте сумму квадратов.
# summ_of_numbers = 0
# for num in comprehension_numbers:
#     summ_of_numbers += num

summ_of_numbers_2 = sum(comprehension_numbers_2)

# print(summ_of_numbers)
print(summ_of_numbers_2)
