# def is_perfect_number(number):
#     divisors_sum = 0
#
#     for divisor in range(1, number):
#         if number % divisor == 0:
#             divisors_sum += divisor
#
#     if divisors_sum == number:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# num = int(input())
# print(is_perfect_number(num))

divisors = []
num = int(input())

for i in range(1, num // 2+1):
    if num % i == 0:
        divisors.append(i)
if sum(divisors) == num:
    print("We have a perfect number!")
else:
    print("It\'s not so perfect.")
