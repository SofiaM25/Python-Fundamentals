message_number = int(input())
message = ""

for num in range(1, message_number +1):
    number = int(input())
    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)
