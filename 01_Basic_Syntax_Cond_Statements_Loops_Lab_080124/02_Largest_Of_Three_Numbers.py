first_num = int(input())
second_num = int(input())
third_num = int(input())

max_number = 0
if first_num > second_num and first_num > third_num:
    max_number = first_num
elif second_num > first_num and second_num > third_num:
    max_number = second_num
else:
    max_number = third_num
print(max_number)

# num1, num2, num3 = int(input()), int(input()), int(input())
# print(max(num1, num2, num3))
    