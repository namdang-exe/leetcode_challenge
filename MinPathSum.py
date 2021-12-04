# DP tabulation
# Bottom up approach
# O(mn) time
# O(mn) space
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        # Make the out_of_bound grid = inf
        for row_i in range(m):
            dp[row_i][n] = float('inf')
        for col_j in range(n):
            dp[m][col_j] = float('inf')
        dp[m][n-1] = 0
        
        # fill in dp
        for row_i in range(m)[::-1]:
            for col_j in range(n)[::-1]:
                dp[row_i][col_j] = min(dp[row_i+1][col_j], dp[row_i][col_j+1]) + grid[row_i][col_j]
                
        return dp[0][0]
    
