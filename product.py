class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f'Товар: {self.name} ,Баасы: {self.price} \n Дана: {self.quantity}')

    def sell(self, newquantity):
        if newquantity < self.quantity:
            self.quantity -= newquantity
            print(f'Дана сатылды: {newquantity}')
        else:
            print('Тавар жетбейт')

