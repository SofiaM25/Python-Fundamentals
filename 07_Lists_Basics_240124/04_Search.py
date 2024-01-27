number_of_strings = int(input())
word = input()
list1 = []
for string in range(number_of_strings):
    current_string = input()
    list1.append(current_string)
print(list1)

for index in range(len(list1) -1, -1, -1):
    element = list1[index]
    if word not in element:
        list1.remove(element)
print(list1)
