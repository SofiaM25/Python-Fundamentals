first_employee_count = int(input())
second_employee_count = int(input())
third_employee_count = int(input())
total_count = first_employee_count + second_employee_count + third_employee_count
time_needed = 0

students_count = int(input())
while True:
    if students_count <= 0:
        break
    students_count -= total_count
    time_needed += 1

    if time_needed % 4 == 0:
        time_needed += 1


print(f"Time needed: {time_needed}h.")
