# DP
# Make an array to keep track of the frequency
# Then the problem turned into House Robber
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # create an array for frequency
        # since the number +1 and number - 1 are deleted
        # which means we can't add their value
        # this is similar to the neighbor constraint in House Robber problem
        m = max(nums) + 1
        freq = [0] * m
        for n in nums:
            freq[n] += 1
        # TODO: edge cases
        
        # DP
        dp = [0] * m
        dp[1] =  freq[1]
        for i in range(2, m):
            dp[i] = max(i*freq[i] + dp[i-2], dp[i-1])
            
        return dp[-1]
        
