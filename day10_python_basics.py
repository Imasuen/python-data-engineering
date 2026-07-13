# Exercise 1 - Variables

name = "Ovbokhan"
age = 35
country = "Nigeria"

print(name)
print(age)
print(country)


# Exercise 2 - f-strings

name = "Ovbokhan"
role = "Data Engineer"

print(f"My name is {name} and I am becoming a {role}.")


# Exercise 3 - Lists

products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headset"
]

for product in products:
    print(product)


# Exercise 4 - Dictionaries

customer = {
    "name": "John Smith",
    "city": "London",
    "age": 32
}

print(customer["name"])
print(customer["city"])
print(customer["age"])


# Exercise 7 - Loop and function

prices = [850, 45, 25, 220]
quantities = [1, 2, 3, 1]


def calculate_order_revenue(price, quantity):
    return price * quantity


for price, quantity in zip(prices, quantities):
    revenue = calculate_order_revenue(price, quantity)
    print(f"Order revenue: £{revenue}")


# Mini Challenge

product_sales = [
    {"name": "Laptop", "price": 850, "quantity": 1},
    {"name": "Mouse", "price": 25, "quantity": 3},
    {"name": "Monitor", "price": 220, "quantity": 1}
]


def calculate_product_revenue(product):
    return product["price"] * product["quantity"]


for product in product_sales:
    revenue = calculate_product_revenue(product)
    print(f'{product["name"]}: £{revenue}')

total_revenue = sum(
    calculate_product_revenue(product)
    for product in product_sales
)

print(f"Total revenue: £{total_revenue}")