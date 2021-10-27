def connected_components_count(graph):
  count = 0
  visited = set()
  # iterative through the node 
  for node in graph:
    if explore(graph, node, visited):
      count += 1
  return count
  
def explore(graph, node, visited):
  # dfs recursive
  if node in visited: return False
  visited.add(node)
  for neighbor in graph[node]:
    explore(graph, neighbor, visited)
  return True

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
