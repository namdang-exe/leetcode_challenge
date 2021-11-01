def isPalindrome(s):
    # recursive
    
    # base case
    if len(s) == 0 or len(s) == 1:
        return True
    
    if s[0] == s[len(s) -1]:
        return isPalindrome(s[1:len(s)-1])
    
    return False


s = "racecar"
print(isPalindrome(list(s)))
