numbers = int(input())
numbers_list = []

for number in range(numbers):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()
filtered = []

if command == "even":
    for number in numbers_list:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in numbers_list:
        if number % 2 != 0:
            filtered.append(number)
elif command == "positive":
    for number in numbers_list:
        if number >= 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers_list:
        if number < 0:
            filtered.append(number)
print(filtered)

# n = int(input())
# command_even = "even"
# command_odd = "odd"
# command_positive = "positive"
# command_negative = "negative"
# numbers = [int(input()) for _ in range(n)]
# filtered_numbers = []
# command = input()
#
# for num in numbers:
#     filtered_command = (
#         (command == command_even and num % 2 == 0) or
#         (command == command_odd and num % 2 != 0) or
#         (command == command_positive and num >= 0) or
#         (command == command_negative and num < 0)
#     )
#     if filtered_command:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)
