n = 2

# Brute force recufsive solution
def climb_stairs(i, n):
    if i > n:
        return 0
    if i == n:
        return 1
    return climb_stairs(i + 1, n) + climb_stairs(i + 2, n)


print(climb_stairs(0, 38))
