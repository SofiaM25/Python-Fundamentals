MAX_SIZE_WAGON = 4

people = int(input())
wagons = [int(num) for num in input().split()]

for i in range(len(wagons)):
    free_spaces = MAX_SIZE_WAGON - wagons[i]

    if people >= free_spaces:
        wagons[i] += free_spaces
    else:
        wagons[i] += people

    people -= free_spaces

    if people <= 0 and (i != len(wagons) - 1 or wagons[i] < MAX_SIZE_WAGON):
        print("The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*wagons)
