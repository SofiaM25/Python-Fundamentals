number_of_strings = int(input())

for i in range(number_of_strings):
    string_name = input()
    if "," in string_name or "." in string_name or "_" in string_name:
        print(f"{string_name} is not pure!")
    else:
        print(f"{string_name} is pure.")
