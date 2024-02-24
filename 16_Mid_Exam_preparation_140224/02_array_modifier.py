array = [int(num) for num in input().split()]
command = input().split()

while command[0] != "end":
    action = command[0]
    if action == "swap":
        first_index, second_index = int(command[1]), int(command[2])
        array[first_index], array[second_index] = \
            array[second_index], array[first_index]
    elif action == "multiply":
        first_index, second_index = int(command[1]), int(command[2])
        array[first_index] *= array[second_index]
    elif action == "decrease":
        array = [num - 1 for num in array]

    command = input().split()


print(", ".join((str(number) for number in array)))

