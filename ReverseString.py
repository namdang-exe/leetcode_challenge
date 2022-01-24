from typing import List
def reverseString(s: List):
    # recursive
    
    # base case
    if len(s) == 0: return ""
    
    return reverseString(s[1:]) + s[0]

s="hello"
print(reverseString(list(s)))
