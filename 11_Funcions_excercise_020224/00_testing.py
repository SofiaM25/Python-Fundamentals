def add_numbers(x, y):
    """Adds two numbers and  returns the result"""
    return x + y


result = add_numbers(3, 5)
print("Result:", result)
print(add_numbers.__doc__)


def greet(name="World"):
    return f"Hello, {name}!"


print(greet())
print(greet("Mike"))


def greet(name, message="Hello"):
    return f"{message}, {name}!"


print(greet("Alice"))
print(greet("Mike", message="Hi there"))


def add(x, y):
    return x + y


add_lambda = lambda x, y: x + y
print(add(5, 7))
print(add_lambda(5, 10))

nums = [1, 2, 3, 4, 5, 6]
double_numbers = list(map(lambda x: x * 2, nums))
print(double_numbers)


def count_recursive(n):
    if n == 1:
        print(n)

    else:
        count_recursive(n - 1)
        print(n)


count_recursive(10)


def calculate_stats(number):
    total_sum = sum(number)
    average = total_sum/len(number)
    max_number = max(number)
    min_number = min(number)

    return total_sum, average, max_number, min_number


data = [10, 20, 30, 40, 550, 60]
total, average, max_number, min_number = calculate_stats(data)

print("Data", data)
print("Total", total)
print("Average", average)
print("Maximum", max_number)
print("Minimum", min_number)


def outer_function(x):

    def inner_function(y):
        return y * 2

    result1 = inner_function(x)
    return result1


output = outer_function(7)
print(output)

numbers = list(map(int, input().split(", ")))  # map converts strings in integers in this case
print(numbers)

