def validParen(s):
    s = list(s)
    hash_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    open_p = '(', '[', '{'
    i = 0
    stack = []
    # ( ( ( ) ) )
    while i < len(s):
        if s[i] in open_p:
            stack.append(s[i])
        # Closing bracket
        else:
            # Check if the stack is empty
            if len(stack) == 0:
                return False
            if stack.pop() != hash_map[s[i]]:
                return False
        i += 1
    if len(stack) != 0:
        return False
    return True


s = "(((())))"
print(validParen(s))
