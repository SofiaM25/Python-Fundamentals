year = int(input())
# while True:
#     year += 1
#     digit_found = ""
#     is_happy_year = True
#     for digit in str(year):
#         if digit in digit_found:
#             is_happy_year = False
#             break
#         digit_found += digit
#     if is_happy_year:
#         break
# print(year)

while True:
    year += 1
    year_as_str = str(year)
    if len(year_as_str) == len(set(year_as_str)):
        break
print(year)
