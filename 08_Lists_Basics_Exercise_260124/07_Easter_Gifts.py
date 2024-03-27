# def out_of_stock_action(easter_gifts_list, curr_gift):
#     for i in range(len(easter_gifts_list)):
#         if curr_gift in easter_gifts_list:
#             index = easter_gifts_list.index(curr_gift)
#             new_item = "None"
#             easter_gifts_list[index] = new_item
#     return easter_gifts_list
#
#
# easter_gifts = input()
#
# while True:
#     action = input()
#     if action == "No Money":
#         break
#
#     action = action.split()
#     if action[0] == "OutOfStock":
#         gift = action[1]
#         easter_gifts = out_of_stock_action(easter_gifts, gift)
#
#     elif action[0] == "Required":
#         old_gift = action[1]
#         new_gift = action[2]
#         pass
#     elif action[0] == "JustInCase":
#         new_gift = action[1]
#         pass
#
# print(f''.join(easter_gifts))


gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for i in range(len(gifts)):
            if command[1] in gifts[i]:
                gifts[i] = "None"
    elif "Required" in command:
        for i in range(len(gifts)):
            if i == int(command[2]):
                gifts[i] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]
    command = input()
while "None" in gifts:
    gifts.remove("None")
for i in gifts:
    print(i, end=" ")
