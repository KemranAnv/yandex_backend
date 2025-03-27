class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_info(self):
        text = f'{self.name} (в наличии: {self.quantity})'
        return text


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    def __init__(self, name, quantity, weight):
        self.weight = weight
        super().__init__(name, quantity)

    def get_weight(self):
        text = (f'{self.name} (в наличии: {self.quantity}). '
                f'Вес: {self.weight} кг')

        # Product.get_info(self)
        return text


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, name, quantity, size):
        self.size = size
        super().__init__(name, quantity)

    def get_size(self):
        text = (f'{self.name} (в наличии: {self.quantity}). '
                f'Размер: {self.size}')

        # Product.get_info(self)

        return text


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
