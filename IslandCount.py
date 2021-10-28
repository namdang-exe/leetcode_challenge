def island_count(grid):
  # dfs recursive
  visited = set()
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      # if the block is L, then explore
      if explore(grid, r, c, visited):
        count += 1
  return count
      
      
def explore(grid, r, c, visited):
  # dfs recursive
  row_in_bounds = 0 <= r < len(grid)
  col_in_bounds = 0 <= c < len(grid[0])
  if not row_in_bounds or not col_in_bounds: return False

  # visited: {'0,0', '0,1'}
  if f"{r},{c}" in visited:
    return False
  visited.add(f"{r},{c}")
  
  if grid[r][c] == 'W':
    return False

  explore(grid, r+1, c, visited)
  explore(grid, r-1, c, visited)
  explore(grid, r, c+1, visited)
  explore(grid, r, c-1, visited)
  
  return True


