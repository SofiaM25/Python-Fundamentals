# Problem 2 - Numbers
numbers = list(map(int, input().split()))
command = input().split()
while command[0] != "Finish":
    value = int(command[1])
    if command[0] == "Add":
        numbers.append(value)
    elif command[0] == "Remove":
        numbers.remove(value)
    elif command[0] == "Replace":
        replacement = int(command[2])
        index_of_value = numbers.index(value)
        numbers[index_of_value] = replacement
    elif command[0] == "Collapse":
        numbers = [num for num in numbers if num >= value]
        # for index in range(len(numbers) - 1, - 1 - 1):
        #     if numbers[index] < value:
        #         numbers.pop(index)
    command = input().split()
print(*numbers, sep=" ")