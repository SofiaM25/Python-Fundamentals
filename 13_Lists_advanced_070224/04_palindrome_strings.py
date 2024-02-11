words = input().split()
palindrome = input()

palindromes_list = [word for word in words if word == "".join(reversed(word))]
print(palindromes_list)
print(f"Found palindrome {palindromes_list.count(palindrome)} times")
