# https://pastebin.com/vrxNF4bB

energy = int(input())
battles_won = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {energy}")
        break
    elif energy >= int(distance):
        battles_won += 1
        energy -= int(distance)
        if battles_won % 3 == 0:
            energy += battles_won
    elif energy < int(distance) or energy <= 0:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break
