lines = int(input())
is_balanced = True
last_bracket = ""
for _ in range(lines):
    string = input()
    if string not in ["(", ")"]:
        continue
    if last_bracket == "" and string == ")" or last_bracket == string:
        is_balanced = False
        break
    last_bracket = string
if not is_balanced:
    print("UNBALANCED")
else:
    print("BALANCED")
