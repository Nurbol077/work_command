class Order:
    def __init__(self, order_id, customer_name, total):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total = total
    def calculate_total(self):
        return f'{self.total} сом'
    def show_order(self):
        print(f'Заказ: {self.order_id} кардар: {self.customer_name} жалпы сумма: {self.total}сом')
