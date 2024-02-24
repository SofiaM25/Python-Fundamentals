def journal_list():
    journal = input().split(", ")

    while True:
        command = input().split(" - ")
        if command[0] == "Craft!":
            break
        action = command[0]
        item = command[1]
        if action == "Collect":
            if item not in journal:
                journal.append(item)
        elif action == "Drop":
            if item in journal:
                journal.remove(item)
        elif action == "Combine Items":
            old_item, new_item = item.split(":")
            if old_item in journal:
                old_item_index = journal.index(old_item)
                journal.insert(old_item_index + 1, new_item)
        elif action == "Renew":
            if item in journal:
                journal.remove(item)
                journal.append(item)

    return journal


print(", ".join(journal_list()))


# journal = input().split(", ")
# command = input().split(" - ")
# while command[0] != "Craft!":
#
#     action = command[0]
#     item = command[1]
#
#     if action == "Collect":
#         if item not in journal:
#             journal.append(item)
#     elif action == "Drop":
#         if item in journal:
#             journal.remove(item)
#     elif action == "Combine Items":
#         old_item, new_item = item.split(":")
#         if old_item in journal:
#             old_item_index = journal.index(old_item)
#             journal.insert(old_item_index + 1, new_item)
#     elif action == "Renew":
#         if item in journal:
#             journal.remove(item)
#             journal.append(item)
#
#     command = input().split(" - ")
#
# print(*journal, sep=", ")
