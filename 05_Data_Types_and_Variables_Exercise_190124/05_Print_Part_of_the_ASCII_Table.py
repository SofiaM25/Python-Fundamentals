start_char = int(input())
end_char = int(input())

# for current_char in range(start_char, end_char + 1):
#     print(f"{chr(current_char)}", end=" ")

# print()

final_string = ""
# for current_char in range(start_char, end_char + 1):
#     final_string += f"{chr(current_char)} "
# print(final_string.rstrip())

for current_char in range(start_char, end_char + 1):
    final_string += f"{chr(current_char)} "
print(final_string[:-1])
