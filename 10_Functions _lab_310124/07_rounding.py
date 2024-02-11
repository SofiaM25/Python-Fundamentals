def rounded_numbers():
    return [round(float(number)) for number in numbers]


numbers = input().split()
print(rounded_numbers())
