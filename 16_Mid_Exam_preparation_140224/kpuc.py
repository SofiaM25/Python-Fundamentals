def final_print():
    if total_people > total_seats:
        return f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join(map(str, wagons))}"
    elif people_waiting == 0 and is_full:
        return " ".join(map(str, wagons))
    else:
        return f"The lift has empty spots!\n{' '.join(map(str, wagons))}"


people_waiting = int(input())
current_state = input()

wagons = [int(wagon) for wagon in current_state.split()]

total_seats = len(wagons) * 4
total_people = sum(wagons) + people_waiting

for i in range(len(wagons)):
    while wagons[i] < 4 and people_waiting > 0:
        wagons[i] += 1
        people_waiting -= 1

is_full = True
for w in wagons:
    if w < 4:
        is_full = False
        break


print(final_print())
