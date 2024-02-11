def to_do():
    to_do_list = []

    while True:
        note = input()

        if note == "End":
            break

        to_do_list.append(note)
    sorted_notes = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
    sorted_notes = [note.split("-")[1] for note in sorted_notes]
    return sorted_notes


result = to_do()
print(result)

