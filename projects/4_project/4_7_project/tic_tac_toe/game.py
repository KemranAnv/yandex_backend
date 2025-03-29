# tic_tac_toe game

from gameparts import Board

# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError.
from gameparts import FieldIndexError

# Добавился ещё один импорт - исключение CellOccupiedError.
from gameparts import CellOccupiedError


# def save_result(result):
#     """Сохраняет результат игры в файл result.txt"""
#     with open('results.txt', 'a', encoding='utf-8') as file:
#         file.write(result + '\n')  # Добавляем новую строку после записи
#         file.close()

def save_result(result):
    # Открыть файл results.txt в режиме "добавление".
    file = open('results.txt', 'a', encoding='utf-8')

    # Записать в файл содержимое переменной result.
    file.write(result + '\n')
    file.close()


# Всё, что ниже этой инструкции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
def main():
    # Создание игрового поля - объект класса Board.
    game = Board()

    # Переменная, в которой по умолчанию будет храниться значение X
    # # Первыми ходят крестики.
    current_player = 'X'

    # Флаговая переменная со значением по умолчанию True.
    # Она понадобится для управления основным циклом игры.
    # Пока поднят флаг (running = True) — игра продолжается,
    # иначе цикл останавливается
    running = True

    # Отрисовка поля в терминале.
    game.display()

    # Запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            # В этом блоке содержатся операции,
            # которые могут вызвать исключение.
            try:
                # Пользователь вводит значение номера строки.
                row = int(input('Введите номер строки: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if row < 0 or row >= game.field_size:
                    # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError

                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError

                # Проверка, занята ли ячейка.
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError

            # Если возникает исключение FieldIndexError...
            except FieldIndexError:
                # ...выводятся сообщения...
                print('Значение должно быть неотрицательным и меньше '
                      f'{game.field_size}'
                      )
                print('Введите значение для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        # В метод make_move передаются координаты.
        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player.
        game.make_move(row, column, current_player)

        # Перерисовать поле с учётом сделанного хода.
        game.display()

        # После каждого хода надо делать провекру на победу и на ничью.
        if game.check_win(current_player):
            result = (f'Победили {current_player}!')
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = ('Ничья!')
            print(result)
            save_result(result)
            running = False

        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
