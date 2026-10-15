class Cart:
    def __init__(self, customer_name, total_price):
        self.customer_name = customer_name
        self.total_price = total_price
    def add_product(self, price):
        self.total_price += price
        print(f'Товар кошулду: {price} com')
    def show_total_price(self):
        print(f'Клиент: {self.customer_name}')
        print(f'Жалпы сумма: {self.total_price}')
