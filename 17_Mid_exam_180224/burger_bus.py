number_of_cities = int(input())
total_income = 0
total_expenses = 0

for current_city in range(1, number_of_cities + 1):
    city = input()
    current_owner_income = float(input())
    current_owner_expenses = float(input())
    if current_city % 3 == 0 and current_city % 5 != 0:
        current_owner_expenses *= 1.5
    if current_city % 5 == 0:
        current_owner_income *= 0.90

    total_income += current_owner_income
    total_expenses += current_owner_expenses

    total_city_profit = current_owner_income - current_owner_expenses
    print(f"In {city} Burger Bus earned {total_city_profit:.2f} leva.")


total_profit = total_income - total_expenses
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
