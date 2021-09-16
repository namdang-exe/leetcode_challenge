s = "{[]}"

hash_map = {
    ')': '(', ']': '[', '}': '{'
}


def get_key(val):
    for key, value in hash_map.items():
        if val == value:
            return key


s = list(s)
# Pop until the list is empty
# But it doesn't detect the wrong order
i = 0
while s and i <= len(s):
    if get_key(s[0]) in s:
        s.remove(get_key(s[0]))
        s.pop(0)
    i += 1

if len(s) == 0:
    print("Valid")
else:
    print("Invalid")
