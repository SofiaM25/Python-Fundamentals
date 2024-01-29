money_string = input().split(", ")
# money_as_integers = [int(money) for money in input().split(", ")]
count_of_beggars = int(input())
money_as_integer = []

for money in money_string:
    money_as_integer.append(int(money))
final_sums = []
start_index = 0
for beggar in range(count_of_beggars):
    beggar_sum = 0
    for index in range(start_index, len(money_as_integer), count_of_beggars):
        beggar_sum += money_as_integer[index]
    final_sums.append(beggar_sum)
    start_index += 1
print(final_sums)
