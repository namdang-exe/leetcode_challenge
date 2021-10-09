# Brute force approach, O(n * k)
def checkInclusion(s1: str, s2: str) -> bool:
    i = 0
    while i + len(s1) <= len(s2):
        temp = list(s1[:])
        for l in s2[i:i + len(s1)]:
            # letter can be repeated
            if l in temp:
                temp.remove(l)
            else:
                pass
        if len(temp) == 0:
            return True
        i += 1
    return False


s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))
