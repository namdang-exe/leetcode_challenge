# Brute force
from typing import List


def shiftingLetters(s: str, shifts: List[int]) -> str:
    def shiftLet(s, n):
        return chr((ord(s) + n - 97) % 26 + 97)

    s = list(s)
    for i in range(len(s)):
        for j in range(i + 1):
            s[j] = shiftLet(s[j], shifts[i])
    return ''.join(s)

print(shiftingLetters(s, shifts))