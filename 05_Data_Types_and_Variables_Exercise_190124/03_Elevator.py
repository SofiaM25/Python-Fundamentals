import math
people = int(input())
capacity = int(input())
courses_necessary = math.ceil(people / capacity)
print(courses_necessary)
