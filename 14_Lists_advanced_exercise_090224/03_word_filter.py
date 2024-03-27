words = input().split()

list_words = [word for word in words if len(word) % 2 == 0]
# print(*list_words, sep="\n")
print("\n".join(list_words))



