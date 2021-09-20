n = 5

# Dynamic Programming
one, two = 1, 1
for i in range(n - 1):
    temp = one
    one = one + two
    two = temp

print(one)
