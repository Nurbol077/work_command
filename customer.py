class Customer:
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.balance = balance
    def show_info(self):
        print(f'Аты:{self.name}\nТелефон:{self.phone}\nБаасы:{self.balance}')
    def buy_price(self, price):
        if self.balance <= price:
            print('сатып алдын')
        else:
            print('акчан жетпейт')

a = Customer('iphone', '18 про макс', 10000)
a.show_info()
a.buy_price(2000)



