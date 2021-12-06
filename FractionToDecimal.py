class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, rem = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator*denominator < 0 else ""
        stack = []
        result = [sign+str(n), '.'] #  ["-2", ".", "repeating parts"]

        while rem != 0 and rem not in stack: # only run when these 2 are fulfil
            stack.append(rem)
            n, rem = divmod(rem*10, abs(denominator))
            result.append(str(n))
        # in case of recurring decimal
        if rem != 0:   
            idx = stack.index(rem)
            result.insert(idx+2, "(")
            result.append(")")
        # ico whole number
        if not stack:
            return "".join(result).replace(".", "")
        return "".join(result)
