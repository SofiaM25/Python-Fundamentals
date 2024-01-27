lines = int(input())
letters_sum = 0
for i in range(1, lines + 1):
    letter = input()
    letters_sum += ord(letter)
print(f"The sum equals: {letters_sum}")
