command = ""
coffee_counter = 0

while command != "END":
    command = input()
    if str.lower(command) == "coding" or str.lower(command) == "dog"\
            or str.lower(command) == "cat" or str.lower(command) == "movie":
        if str.islower(command):
            coffee_counter += 1
        else:
            coffee_counter += 2
    else:
        continue

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)




