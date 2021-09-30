def unlockKey(k):
    dig = []
    while k != 0:
        dig.append(str(k % 10))
        k //= 10
    sorted_dig = sorted(dig)
    return int(''.join(sorted_dig))

k = 756
print(unlockKey(k))
print(type(unlockKey(k)))