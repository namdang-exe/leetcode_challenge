def shift(s, n):
    # wrap around alphabet
    return chr((ord(s) + n - 97) % 26 + 97)


def cylicShift(strings):
    words = strings.split()
    out = []
    for w in words:
        w = list(w)
        # this returns an array
        w_idx = [i for i in range(len(w))][::-1]
        temp = []
        for letter, index in zip(w, w_idx):
            temp.append(shift(letter, index))
        # join will return a string
        out.append(''.join(temp))
    return ' '.join(out)

    # w = "yum"
    # w = list(w)
    # # "muy"
    # reverse_w = w[::-1]
    # for i in range(len(reverse_w)):
    #     hash_map[reverse_w[i]] = i
    # print(hash_map)


strings = "yum feed"
print(cylicShift(strings))
