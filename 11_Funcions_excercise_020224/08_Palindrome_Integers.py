def palindrome_func(lst):
    result = ''

    for num in lst:
        if str(num) == str(num)[::-1]:
            result += "True\n"
        else:
            result += "False\n"


list_of_palindromes = list(map(int, input().split(", ")))
print(palindrome_func(list_of_palindromes))

# def is_palindrome(num):
#     return str(num) == str(num)[::-1]
#
#
# def palindrome_function(lst):
#     return "\n".join(["True" if is_palindrome(num) else "False" for num in lst])
#
#
# list_of_palindromes = list(map(int, input().split(", ")))
# print(palindrome_func(list_of_palindromes))
