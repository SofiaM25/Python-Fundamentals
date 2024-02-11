def check_employee_happiness():

    employee_happiness = list(map(int, input().split()))
    improvement_factor = int(input())

    improved_happiness = [e * improvement_factor for e in employee_happiness]
    average_happiness = sum(improved_happiness) / len(improved_happiness)

    happy_count = sum(h >= average_happiness for h in improved_happiness)
    total_count = len(improved_happiness)

    message = "happy" if happy_count >= total_count / 2 else "not happy"
    result = f"Score: {happy_count}/{total_count}. Employees are {message}!"

    return result


result = check_employee_happiness()
print(result)
