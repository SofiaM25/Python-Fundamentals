key = int(input())
lines = int(input())
decrypted_message = []

for i in range(1, lines + 1):
    character = ord(input())
    new_character = chr(character + key)
    decrypted_message.append(new_character)

print("".join(map(str, decrypted_message)))
