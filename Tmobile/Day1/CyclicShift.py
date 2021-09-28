def shift(s, n):
    return chr((ord(s) - ord('a') + n) % 26 + ord('a'))


def shiftLetter(s):
    # get a list of words, separated by space " "
    words = s.split()
    out = []
    for w in words:
        temp = []
        letters = list(w)
        # Do it backward
        # Instead of yum
        # muy
        # 0 1 2
        reversed_l = letters[::-1]
        for i in range(len(reversed_l)):
            shifted_l = shift(reversed_l[i], i)
            temp.append(shifted_l)
        # Reverse back at the end
        out.append(''.join(temp[::-1]))
    return ' '.join(out)


s = "yum feed"
print(shiftLetter(s))
