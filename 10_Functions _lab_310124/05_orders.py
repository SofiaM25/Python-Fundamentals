

def orders(order, price):
    return price * quantity


type_order = input()
quantity = int(input())

if type_order == "coffee":
    price = 1.5
elif type_order == "water":
    price = 1.0
elif type_order == "coke":
    price = 1.40
elif type_order == "snacks":
    price = 2.0

print(f"{orders(type_order, price):.2f}")
