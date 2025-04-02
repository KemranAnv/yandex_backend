def fibonacci(n):
    # Допишите функцию.

    if n <= 0:
        return

    a_number = 0
    yield a_number

    if n == 1:
        return

    b_number = 1
    yield b_number

    for _ in range(2, n):
        a_number, b_number = b_number, a_number + b_number
        yield b_number


sequence = fibonacci(10)
for number in sequence:
    print(number)
