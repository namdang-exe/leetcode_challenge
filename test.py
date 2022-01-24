# output = [[]]
# output[0] = output[0] + [1] + [2]
# print(output)
# output.append([2])
# print(output)
# print(min(output[0]))
from typing import List


def cons_mat(s, m, n):
    mat = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp += [s]
            s += 1
        mat.append(temp)
    return mat


def multiMat(s, m, n):
    # [[0,0,0], [0,0,0], [0,0,0]]
    out = [[0 for _ in range(m)] for _ in range(n)]
    print(out)


# multiMat(1, 3, 3)
#
# print(cons_mat(4, 3, 2))

def shift_char(s, n):
    return chr((ord(s) - 97 + n) % 26 + 97)

    # print(shift_char('y', 2))
    # test enum
    # letters = ['a', 'b', 'c']
    # idx = [5, 2, 3]
    # for i, val in enumerate(zip(letters, idx)):
    #     l, s = val
    #     print(l, s, i)
    #
    # for l, s, i in zip(letters, idx, range(len(letters))):
    #     print(l, s, i)


def shiftingLetters(s: str, shifts: List[int]) -> str:
    def shiftLet(s, n):
        return chr((ord(s) + n - 97) % 26 + 97)

    s = list(s)
    for l, shift, i in zip(s, shifts, range(len(s))):
        for j in range(i+1):
            s[j] = shiftLet(s[j], shift)
    return s


s = "abc"
shifts = [3, 5, 9]
print(shiftingLetters(s, shifts))
