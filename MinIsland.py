def minimum_island(grid):
  # dfs recursive
  visited = set()
  min_size = float('inf')
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = explore(grid, r, c, visited)
      # explore() will return 0 if it is not a proper island 
      if size != 0:
        min_size = min(min_size, size)
      
  return min_size

def explore(grid, r,c, visited):
  # dfs recursive
  
  # Check out of bounds
  row_bounds = 0 <= r < len(grid)
  col_bounds = 0 <= c < len(grid[0])
  if not row_bounds or not col_bounds: return 0
  
  # visited: {'0,0', '0,1'}
  pos = f'{r},{c}'
  if pos in visited: return 0
  visited.add(pos)
  
  # Don't count if it's not land
  if grid[r][c] == 'W': return 0
  
  size = 1
  size += explore(grid, r-1, c, visited)
  size += explore(grid, r+1, c, visited)  
  size += explore(grid, r, c - 1, visited)      
  size += explore(grid, r, c + 1, visited)    
  return size


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2
