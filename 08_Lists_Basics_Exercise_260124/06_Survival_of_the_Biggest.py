# numbers_string = input().split()
# numbers = []
#
# for number in numbers_string:
#     numbers.append(int(number))
# count_remover = int(input())
# for _ in range(count_remover):
#     numbers.remove(min(numbers))
# print(numbers, sep=", ")

numbers = [int(num) for num in input().split()]
remover = int(input())
for _ in range(remover):
    numbers.remove(min(numbers))
    result = ", ".join(map(str, numbers))

print(result)
