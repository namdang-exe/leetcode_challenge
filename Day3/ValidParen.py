class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren = '(', '{', '['
        hash_map = {
            ')': '(', ']':'[', '}':'{'
        }
        s = list(s)
        for i in range(len(s)):
            if s[i] in open_paren:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != hash_map.get(s[i]):
                        return False
        if len(stack) != 0:
            return False
        return True