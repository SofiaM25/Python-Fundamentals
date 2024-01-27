# number = input()
# for n in range(9, -1, -1):
#     for i in number:
#         if int(i) == int(n):
#             print(n, end="")


number = input()
my_list = sorted(number, reverse=True)
for i in my_list:
    print(i, end="")
