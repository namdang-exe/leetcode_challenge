class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos_dp = [0] *n
        neg_dp = [0] *n
        if nums[0] > 0: pos_dp[0] = 1
        if nums[0] < 0: neg_dp[0] = 1
        # notice we ignore num = 0
        res = pos_dp[0]
        
        for i in range(1,n):
            val = nums[i]
            if val < 0:
                neg_dp[i] = max(neg_dp[i], pos_dp[i-1]+1)
                if neg_dp[i-1] > 0: # if there is already a running negative prod
                    pos_dp[i] = max(pos_dp[i], neg_dp[i-1] + 1)
            if val > 0:
                pos_dp[i] = max(pos_dp[i], pos_dp[i-1]+1)
                if neg_dp[i-1] > 0: # there is a running negative prod
                    neg_dp[i] = max(neg_dp[i], neg_dp[i-1] + 1)
            res = max(res, pos_dp[i])
            
        return res
                
