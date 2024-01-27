number_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range(1, number_snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_value = (weight / time_needed) ** quality

    if current_value > max_value:
        max_weight = weight
        max_time = time_needed
        max_quality = quality
        max_value = current_value

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quality})")
