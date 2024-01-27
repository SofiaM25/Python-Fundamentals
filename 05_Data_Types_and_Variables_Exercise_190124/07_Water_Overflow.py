capacity = 255
lines = int(input())

for i in range(lines):
    liquid_added = int(input())
    if capacity < liquid_added:
        print("Insufficient capacity!")
        continue
    capacity -= liquid_added
print(255 - capacity)
