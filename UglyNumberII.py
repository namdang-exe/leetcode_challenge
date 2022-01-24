# Dynamic Programming
# Tabulation aka table

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        i2, i3, i5 = 0, 0, 0
        multi_of_2 = 2
        multi_of_3 = 3
        multi_of_5 = 5
        
        for i in range(1, n):
            min_of_multi = min(multi_of_2, multi_of_3, multi_of_5)
            dp[i] = min_of_multi

            # update multi
            if min_of_multi == multi_of_2: 
                i2 += 1
                multi_of_2 = dp[i2] * 2
            if min_of_multi == multi_of_3: 
                i3 += 1
                multi_of_3 = dp[i3] * 3
            if min_of_multi == multi_of_5: 
                i5 += 1
                multi_of_5 = dp[i5] * 5
            
        return dp[-1]
