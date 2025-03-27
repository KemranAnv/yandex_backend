# tic_tac_toe game

# from parts import Board
from gameparts import Board


# Всё, что ниже этой инструкции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
    # Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()
