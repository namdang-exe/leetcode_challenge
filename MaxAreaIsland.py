class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs recursive
        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.explore(grid, r, c, visited)
                print(size)
                # if size == 0, meaning it is not a proper island, ignore
                if size != 0:
                    max_area = max(max_area, size)
                    
        return max_area
                
    def explore(self, grid, r, c, visited):
        # dfs recursive
        
        # Check out of bounds
        row_bounds = 0 <= r < len(grid)
        col_bounds = 0 <= c < len(grid[0])
        if not row_bounds or not col_bounds: return 0
        
        # visited: {'0,1', '0,2'}
        pos = f'{r},{c}'
        if pos in visited: return 0
        visited.add(pos)
        
        # Don't count if it's a water
        if grid[r][c] == 0: return 0
        
        size = 1
        size += self.explore(grid, r-1, c, visited)
        size += self.explore(grid, r+1, c, visited)        
        size += self.explore(grid, r, c-1, visited)                
        size += self.explore(grid, r, c+1, visited)                

        return size
