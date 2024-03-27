# data = input().split(", ")
# positives = [num for num in data if int(num) >= 0]
# negatives = [num for num in data if int(num) < 0]
# odds = [num for num in data if int(num) % 2 != 0]
# evens = [num for num in data if int(num) % 2 == 0]
#
# print(f"Positive: {', '.join(positives)}")
# print(f"Negative: {', '.join(negatives)}")
# print(f"Even: {', '.join(evens)}")
# print(f"Odd: {', '.join(odds)}")


def positive_numbers(list_of_numbers):
    return ', '.join([num for num in data if int(num) >= 0])


def negative_numbers(list_of_numbers):
    return ', '.join([num for num in data if int(num) < 0])


def even_numbers(list_of_numbers):
    return ', '.join([num for num in data if int(num) % 2 != 0])


def odd_numbers(list_of_numbers):
    return ', '.join([num for num in data if int(num) % 2 == 0])


data = input().split(", ")

print(f"Positive: {positive_numbers(data)}")
print(f"Negative: {negative_numbers(data)}")
print(f"Even: {even_numbers(data)}")
print(f"Odd: {odd_numbers(data)}")
