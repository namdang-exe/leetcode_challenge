# Recursion 
# O(2^mn) time
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def bfs(row, col):
            # breath first search
            # recursion
            
            # base cases
            if row == m or col == n: return float('inf')
            if row == (m -1) and col == (n-1): return grid[row][col]
            
            # recursion
            res = 0
            res = min(bfs(row + 1, col), bfs(row, col + 1)) + grid[row][col]
            
            return res
        return bfs(0,0)
