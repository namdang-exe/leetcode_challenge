"""
ab-cd
a
ba
dcba
"""
from collections import deque

test = "Test1ng-Leet=code-Q!"
reverse_string = deque()
needed_idx = []
for i in range(len(test)):
    if not test[i].isalpha():
        needed_idx.append(i)
    else:
        reverse_string.appendleft(test[i])

for i in needed_idx:
    reverse_string.insert(i, test[i])

print(''.join(reverse_string))
