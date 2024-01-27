number_of_orders = int(input())
coffee_price = 0
total_price = 0
for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 100000 < price_per_capsule or 0.01 > price_per_capsule:
        continue
    if 1 > days or days > 31:
        continue
    if 1 > capsules_per_day or capsules_per_day > 2000:
        continue
    coffee_price = price_per_capsule * days * capsules_per_day
    total_price += coffee_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")
print(f"Total: ${total_price:.2f}")
