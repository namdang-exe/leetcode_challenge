def shift(s, n):
    return chr((ord(s) - ord('a') + n) % 26 + ord('a'))


def shiftLetter(s):
    words = s.split()
    out = []
    for w in words:
        w = list(w)
        reversed_w = w[::-1]
        temp = []
        for idx, letter in enumerate((reversed_w)):
            temp.append(shift(letter, idx))
        out.append(''.join(temp[::-1]))
    return ' '.join(out)


s = "yum feed"
print(shiftLetter(s))
