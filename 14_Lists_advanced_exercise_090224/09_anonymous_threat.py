# def merge_element(elements, start_idx, end_idx):
#     merge_result = ''
#     for idx in range(start_idx, end_idx + 1):
#         merge_result += elements[idx]
#
#     return merge_result
#
#
# words = input().split()
#
# while True:
#     line = input()
#     if line == "3:1":
#         break
#
#     command, first_argument, second_argument = line.split()
#
#     if command == "merge":
#         start_index = int(first_argument)
#         end_index = int(second_argument)
#
#         if start_index >= end_index:
#             continue
#
#         # index validation
#         start_index = max(0, start_index)
#         end_index = min(len(words) - 1, end_index)
#
#         merged_element = merge_element(words, start_index, end_index)
#         remove_counter_operations = end_index - start_index + 1
#         for _ in range(remove_counter_operations):
#             words.pop(start_index)
#         words.insert(start_index, merged_element)
#
#     elif command == "divide":
#         el_index = int(first_argument)
#         partitions = int(second_argument)
#
#         element = words[el_index]
#         elements_parts = []
#         partition_size = len(element) // partitions
#
#         current_partition = ''
#         for index in range((partitions - 1) * partition_size):
#             current_partition += element[index]
#             if len(current_partition) == partition_size:
#                 elements_parts.append(current_partition)
#                 current_partition = ''
#
#         current_partition = ''
#         for i in range((partitions - 1) * partition_size, len(element)):
#             current_partition += element[i]
#
#         elements_parts.append(current_partition)
#
#         words.pop(el_index)
#         for idx1 in range(len(elements_parts)):
#             words.insert(el_index + idx1, elements_parts[idx1])
#
# print(' '.join(words))

text = input().split()
command = input().split()
while command[0] != "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_elements = "".join(text[start_index:end_index + 1])
        # text = text[0:start_index] + [merged_elements] + text[end_index +1]
        text[start_index:end_index + 1] = [merged_elements]
    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        element = text[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                divided_partition.append(
                    element[current_element_index * partition_length: (current_element_index + 1) * partition_length])
            else:
                divided_partition.append(element[current_element_index * partition_length:])
        text[index:index + 1] = divided_partition

    command = input().split()
print(" ".join(text))
