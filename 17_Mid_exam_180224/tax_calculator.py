vehicles = input().split(">>")
vehicle = [str(vehicle) for vehicle in vehicles]
total_tax_collected = 0

for vehicle in vehicles:
    vehicle = vehicle.split()
    curr_vehicle = vehicle[0]
    years_tax = vehicle[1]
    km_traveled = vehicle[2]

    if curr_vehicle == 'family':
        initial_tax = 50
        curr_vehicle_tax = initial_tax - 5 * int(years_tax) + 12 * (int(km_traveled) // 3000)

    elif curr_vehicle == 'heavyDuty':
        initial_tax = 80
        curr_vehicle_tax = initial_tax - 8 * int(years_tax) + 14 * (int(km_traveled) // 9000)

    elif curr_vehicle == 'sports':
        initial_tax = 100
        curr_vehicle_tax = initial_tax - 9 * int(years_tax) + 18 * (int(km_traveled) // 2000)

    else:
        print("Invalid car type.")
        continue

    print(f"A {curr_vehicle} car will pay {curr_vehicle_tax:.2f} euros in taxes.")
    total_tax_collected += curr_vehicle_tax

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
