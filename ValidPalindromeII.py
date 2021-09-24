def validPalindrome(s):
    # 2 Pointers
    left, right = 0, len(s) - 1
    while left < right:
        # if 2 letters are not equal, split the rest into 2 sub string
        if s[left] != s[right]:
            # first substring is without the left pointer current value
            # second substring is without the right point current value
            one, two = s[left + 1: right + 1], s[left: right]
            return one == one[::-1] or two == two[::-1]
        left += 1
        right -= 1
    return True


s = "acxcybycxcxa"
print(validPalindrome(s))
