top_five = 5

numbers = [int(num) for num in input().split()]
avg_num = sum(numbers) / len(numbers)
top_five_list = sorted([x for x in numbers if x > avg_num])

if not top_five_list:
    print("No")
else:
    for num in range(top_five):
        if top_five_list:
            print(top_five_list.pop(), end=" ")
