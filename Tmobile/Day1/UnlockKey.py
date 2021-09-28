def unlockKey(k):
    out = []
    # 756
    while k != 0:
        out.append(str(k % 10))         # 6
        k //= 10 # 75
    out = sorted(out)
    return int(''.join(out))

k = 756
print(unlockKey(k))