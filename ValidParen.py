def get_key(val):
    for key, value in hash_map.items():
        if val == value:
            return key


s = "(){}}{"
hash_map = {
    ')': '(', ']': '[', '}': '{'
}
paren = '(', '[', '{'
s = list(s)
# Pop until the list is empty
i = 0
empty_list = []
while i < len(s):
    if s[i] in paren:
        empty_list.append(s[i])
    else:
        # empty list can't bbe emptied
        if len(empty_list) == 0:
            break
        else:
            if hash_map.get(s[i]) == empty_list[-1]:
                empty_list.pop()
            else:
                break
    i += 1

if len(empty_list) == 0:
    print("Valid")
else:
    print("Invalid")
