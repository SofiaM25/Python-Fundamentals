name = ""
house = ""
while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if len(name) < 5:
        house = "Gryffindor"
    elif len(name) == 5:
        house = "Slytherin"
    elif len(name) == 6:
        house = "Ravenclaw"
    elif len(name) > 6:
        house = "Hufflepuff"
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        print(f"{name} goes to {house}.")



