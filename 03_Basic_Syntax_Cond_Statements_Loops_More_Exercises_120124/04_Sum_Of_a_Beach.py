text = input().lower()
beach_components = ["sand", "water", "fish", "sun"]
counter = 0
# print(sum([text.count(word) for word in beach_components]))
for word in beach_components:
    counter += sum([text.count(word)])
print(f"{counter}")
