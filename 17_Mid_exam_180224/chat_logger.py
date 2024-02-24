messages = []

while True:
    command_line = input().split()

    if command_line[0] == "end":
        break
    current_message = command_line[1]

    if command_line[0] == "Chat":
        messages.append(current_message)

    elif command_line[0] == "Delete":
        if current_message in messages:
            messages.remove(current_message)
        else:
            continue

    elif command_line[0] == "Edit":
        edited_version_message = command_line[2]
        if current_message in messages:
            index = messages.index(current_message)
            messages[index] = edited_version_message
        else:
            continue

    elif command_line[0] == "Pin":
        if current_message in messages:
            messages.remove(current_message)
            messages.append(current_message)
        else:
            continue

    elif command_line[0] == "Spam":
        all_messages = command_line[1:]
        messages = messages + all_messages

print("\n".join(messages))




