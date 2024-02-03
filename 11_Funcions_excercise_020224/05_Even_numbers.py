numbers_as_string = input()
integers_list = [int(i) for i in numbers_as_string.split()]


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


is_it_even = list(filter(is_even, integers_list))
even_numbers_list = []

for current_even_numbers in is_it_even:
    even_numbers_list.append(current_even_numbers)
print(even_numbers_list)


