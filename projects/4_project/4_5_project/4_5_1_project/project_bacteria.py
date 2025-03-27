class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, max_bacteria):
        self.current = 0
        self.max_bacteria = max_bacteria

    # Допишите метод
    def create_new(self):
        if (self.current + 1) <= self.max_bacteria:
            self.current += 1
            print('Добавлена одна бактерия. Количество бактерий в популяции: '
                  f'{self.current}')
        elif (self.current + 1) > self.max_bacteria:
            print('Нет места под новую бактерию')

    # Допишите метод
    def remove_one(self):
        if self.current > 0:
            self.current -= 1
            print('Одна бактерия удалена. Количество бактерий в популяции: '
                  f'{self.current}')
        elif self.current <= 0:
            print('В популяции нет бактерий, удалять нечего')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
