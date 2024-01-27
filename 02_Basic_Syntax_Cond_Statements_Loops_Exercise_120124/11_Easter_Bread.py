budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = (1.25 * price_flour) / 4
colored_eggs_count = 0
loaves_of_bread_count = 0
total_cost = price_milk + price_eggs + price_flour

while total_cost <= budget:
    loaves_of_bread_count += 1
    colored_eggs_count += 3
    budget -= total_cost
    if loaves_of_bread_count % 3 == 0:
        colored_eggs_count -= loaves_of_bread_count - 2

print(f"You made {loaves_of_bread_count} loaves of Easter bread! Now you have {colored_eggs_count}\
 eggs and {budget:.2f}BGN left.")

