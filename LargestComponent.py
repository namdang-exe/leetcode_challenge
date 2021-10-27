def largest_component(graph):
  visited = set()
  max_size = 0
  # Iterate thru the nodes
  for node in graph:
    size = explore(graph, node, visited)
    max_size = max(max_size, size)
  return max_size


def explore(graph, node, visited):
  if node in visited: return 0
  visited.add(node)
  size = 1
  for neighbor in graph[node]:
    size += explore(graph, neighbor, visited)
  return size
