def fibonacci(n):
    # Допишите функцию.

    list_of_numbers = [0, 1]

    for i in range(n):
        a_number = list_of_numbers[i]
        b_number = list_of_numbers[i+1]
        c_number = a_number + b_number
        list_of_numbers.append(c_number)

    for i in range(n):
        yield list_of_numbers[i]


sequence = fibonacci(10)
for number in sequence:
    print(number)
