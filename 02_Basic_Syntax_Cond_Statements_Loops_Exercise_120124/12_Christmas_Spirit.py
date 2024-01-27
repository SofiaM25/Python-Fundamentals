quantity_of_decorations = int(input())
days_left = int(input())
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
total_cost = 0
christmas_spirit = 0

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += price_ornament_set * quantity_of_decorations
        christmas_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity_of_decorations * (price_tree_skirt + price_tree_garland)
        christmas_spirit += 3 + 10
    if current_day % 5 == 0:
        total_cost += price_tree_lights * quantity_of_decorations
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        total_cost += price_tree_lights + price_tree_garland + price_tree_skirt
if days_left % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
