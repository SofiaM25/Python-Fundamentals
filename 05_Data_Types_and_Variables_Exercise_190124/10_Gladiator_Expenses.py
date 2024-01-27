lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0

for current_fight in range(1, lost_fights_count + 1):
    if current_fight % 2 == 0:
        broken_helmet_count += 1
    if current_fight % 3 == 0:
        broken_sword_count += 1
    if current_fight % (2 * 3) == 0:
        broken_shield_count += 1
        if broken_shield_count % 2 == 0:
            broken_armor_count += 1

total_expenses = helmet_price * broken_helmet_count \
                 + sword_price * broken_sword_count \
                 + shield_price * broken_shield_count \
                 + armor_price * broken_armor_count
print(f"Gladiator expenses: {total_expenses:.2f} aureus")

# number_of_lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# total_helmet_broken = number_of_lost_fights // 2
# total_sword_broken = number_of_lost_fights // 3
# total_shield_broken = number_of_lost_fights // (2*3)
# total_armor_broken = total_shield_broken // 2
# expenses = total_helmet_broken * helmet_price + \
#            total_sword_broken * sword_price + \
#            total_shield_broken * shield_price + \
#            total_armor_broken * armor_price
# print(f"Gladiator expenses: {expenses:.2f} aureus")
