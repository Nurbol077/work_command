from product import Product
from cart import Cart
from customer import Customer
from order import Order


# Товар тузуу

product = Product('Наушник', 1000, 10)
product.show_info()

print('#' * 20)

# Кардар тузуу
customer = Customer('Асан', '0700556677', 5000)
customer.show_info()

print('#' * 20)

# Корзина

cart = Cart(customer.name)
cart.add_product(product.price)
cart.show_total_price()

print('#' * 20)

customer.buy_price(cart.total_price)

order = Order(1, customer.name, cart.total_price)
order.show_order()
