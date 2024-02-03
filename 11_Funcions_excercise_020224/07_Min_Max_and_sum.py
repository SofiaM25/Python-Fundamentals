numbers_as_string = input()
numbers_as_integers = [int(num) for num in numbers_as_string.split()]


def data(number):
    minimum_number = min(number)
    maximum_number = max(number)
    sum_all_numbers = sum(number)

    return minimum_number, maximum_number, sum_all_numbers


minimum_number, maximum_number, sum_all_numbers = data(numbers_as_integers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_all_numbers}")


