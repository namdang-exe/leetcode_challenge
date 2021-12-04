# DP tabulation
# Bottom up approach
# 1D DP
# O(mn) time
# O(n) space
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * (n+1)
        dp[n-1] = 0
        
        # fill in dp
        for row_i in range(m)[::-1]:
            for col_j in range(n)[::-1]:
                dp[col_j] = min(dp[col_j], dp[col_j + 1]) + grid[row_i][col_j]  
                
        return dp[0]
    
