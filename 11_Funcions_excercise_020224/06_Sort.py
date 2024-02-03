numbers_as_string = input()
integers_list = [int(i) for i in numbers_as_string.split()]


def sorted_numbers(number):
    return sorted(number)


new_list = []
for i in integers_list:
    new_list.append(i)

print(sorted_numbers(new_list))
