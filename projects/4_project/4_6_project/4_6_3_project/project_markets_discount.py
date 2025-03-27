class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, initial_price):
        new_price = initial_price * ((100 - self.__discount) / 100)
        return round(new_price, ndigits=2)

    def set_discount(self, new_discount):
        if new_discount > 80:
            self.__discount = 80
        elif new_discount <= 80:
            self.__discount = new_discount


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)
