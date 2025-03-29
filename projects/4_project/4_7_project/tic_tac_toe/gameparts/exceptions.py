"""Класс который обрабатывает ошибку заполнения поля"""


class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'
