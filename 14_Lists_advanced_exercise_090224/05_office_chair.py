def check_room(number_of_rooms):
    free_chairs = 0
    for number_of_rooms in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        diff = len(free_chairs_in_current_room) - int(visitors)
        if diff < 0:
            print(f"{abs(diff)} more chairs needed in room {number_of_rooms}")
        free_chairs += diff

    return free_chairs


count_of_rooms = int(input())
total_free_chairs = check_room(count_of_rooms)

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
