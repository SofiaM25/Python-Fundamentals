# https://pastebin.com/1fARpz4N

year = "9010"
print(set(year))
print(list(year))
print(year[:2:-1])

# slicing
# sequence[start_index:end_index:step]

my_list = ['apple', 'banana', 'cherry', 'date', '666']
print(my_list[1:3])
print(my_list[0::2])
print(my_list[:3])
print(my_list[3:])
print(my_list[:-5:-1])

a = ['898', 'cat', 'dog', '65.0', '666']
print(a[-1])    # last item in the array
print(a[-2:])   # last two items in the array
print(a[:-2])   # everything except the last two items

word = "cat"
print(word[:1])
print(word[1:])
print(word[0:2])
print(word[:-3:-1])

# tuple - a collection that`s ordered and unchangeable
example_tuple = ("air", "water", "fire")
print(example_tuple)
# list - contains items separated by commas and enclosed with square brackets
example_list = ["air", "water", "fire"]
print(example_list[::-1])
# set - a collection that`s unordered and unindexed, with curly brackets
example_set = {"air", "water", "fire", "water"}
print(example_set)
# dictionary - an ordered, changeable and indexed collection
example_dict = {"name": "Sofia", "age": "34"}
print(example_dict["age"])
