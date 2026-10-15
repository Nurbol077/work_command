class Customer:
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.balance = balance

    def show_info(self):
        print(f'Аты:{self.name}\nТелефон:{self.phone}\nАкчасы:{self.balance}')

    def buy_price(self, price):
        if self.balance >= price:
            print('сатып алдын')
        else:
            print('акчан жетпейт')




