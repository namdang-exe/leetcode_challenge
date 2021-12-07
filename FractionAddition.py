# gcd 
class Solution:
    def fractionAddition(self, expression):
        lst = expression.replace("+", " +").replace("-", " -").split()
        A, B = 0, 1
        for num in lst: # O(n)
            a, b = num.split("/")
            a, b = int(a), int(b)
            A = A*b+B*a
            B *= b
            divisor = math.gcd(A, B) # O(logx)
            A //= divisor
            B //= divisor
        return str(A) + "/" + str(B)
