def process_username_commands(username, commands):

    for commands in commands:
        tokens = commands.split()
        action = tokens[0]

        if action == "Letters":
            case_type = tokens[1]
            if case_type == "Lower":
                username = username.lower()
            elif case_type == "Upper":
                username = username.upper()
            print(username)

        elif action == "Reverse":
            start_index = int(tokens[1])
            end_index = int(tokens[2])
            if 0 <= start_index < len(username) and 0 <= end_index < len(username):
                reversed_substring = username[start_index:end_index + 1][::-1]
                print(reversed_substring)

        elif action == "Substring":
            substring = tokens[1]
            if substring in username:
                username = username.replace(substring, '')
                print(username)
            else:
                print(f'The username {username} doesn\'t contain {substring}.')

        elif action == "Replace":
            char_to_replace = tokens[1]
            username = username.replace(char_to_replace, '-')
            print(username)

        elif action == "IsValid":
            char_to_check = tokens[1]
            if char_to_check in username:
                print("Valid username.")
            else:
                print(f'{char_to_check} must be contained in your username.')

        elif action == "Registration":
            break


initial_username = input()
commands_list = []
while True:
    command = input()
    if command == "Registration":
        break
    commands_list.append(command)

process_username_commands(initial_username, commands_list)
