# Recursion with memoize
# O(mn) time
# O(mn) space

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cache = {} # {(1, 1): 4}
        
        def bfs(row, col):
            # breath first search
            # recursion
            
            if (row, col) in cache: return cache[(row,col)]
            # base cases
            if row == m or col == n: return float('inf')
            if row == (m -1) and col == (n-1): return grid[row][col]
            
            # recursion
            res = 0
            res = min(bfs(row + 1, col), bfs(row, col + 1)) + grid[row][col]
            cache[(row, col)] = res
            
            return cache[(row,col)]
        return bfs(0,0)
