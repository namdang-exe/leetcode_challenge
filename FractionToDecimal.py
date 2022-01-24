class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, rem = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator*denominator < 0 else ""
        remainders = {}
        result = [sign+str(n), '.'] #  ["-2", ".", "repeating parts"]

        while rem != 0 and rem not in remainders: # only run when these 2 are fulfilled
            remainders[rem] = len(result)
            n, rem = divmod(rem*10, abs(denominator))
            result.append(str(n))
        # in case of recurring decimal
        if rem in remainders:   
            idx = remainders[rem]
            result.insert(idx, "(")
            result.append(")")
        # ico whole number
        if not remainders:
            return "".join(result).replace(".", "")
        return "".join(result)
