# total_price_without_taxes = 0
# total_amount_of_taxes = 0
# total_price_with_taxes = 0
#
# while True:
#     command = input()
#     if command == "special" or command == "regular":
#         break
#     current_price = float(command)
#     if current_price < 0:
#         print("Invalid price!")
#         continue
#     total_price_without_taxes += current_price
#     total_amount_of_taxes += 0.2 * current_price
#     total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes
#
# if total_price_with_taxes == 0:
#     print("Invalid order!")
# elif command == "special":
#     total_price_with_taxes = 0.9 * total_price_with_taxes
#     print(f"Congratulations you've just bought a new computer! \n"
#           f"Price without taxes: {total_price_without_taxes:.2f}$ \n"
#           f"Taxes: {total_amount_of_taxes:.2f}$ \n"
#           f"----------- \n"
#           f"Total price: {total_price_with_taxes:.2f}$")
# elif command == "regular":
#     print(f"Congratulations you've just bought a new computer! \n"
#           f"Price without taxes: {total_price_without_taxes:.2f}$ \n"
#           f"Taxes: {total_amount_of_taxes:.2f}$ \n"
#           f"----------- \n"
#           f"Total price: {total_price_with_taxes:.2f}$")

def calculate_order_price(prices):
    prices_without_taxes = sum(prices)
    taxes = sum(price * 0.20 for price in prices)
    return prices_without_taxes, taxes


def computer_store():
    prices = []
    additional_discount = False

    while True:
        command = input().strip().lower()
        if command == "special" or command == "regular":
            if not prices:
                return "Invalid order!"

            additional_discount = True if command == "special" else False
            break

        current_price = float(command)

        if current_price < 0:
            print("Invalid price!")
            continue

        prices.append(current_price)

    price_without_taxes, taxes = calculate_order_price(prices)

    if additional_discount:
        total_price = price_without_taxes + taxes
        total_price *= 0.90
        return total_price, price_without_taxes, taxes
    return price_without_taxes + taxes, price_without_taxes, taxes


def print_receipt(total_price, price_without_additional_taxes, taxes):
    print(f"Congratulations you've just bought a new computer! \n"
          f"Price without taxes: {price_without_additional_taxes:.2f}$ \n"
          f"Taxes: {taxes:.2f}$ \n"
          f"----------- \n"
          f"Total price: {total_price:.2f}$")


result = computer_store()
if isinstance(result, tuple):
    print_receipt(*result)
else:
    print(result)
