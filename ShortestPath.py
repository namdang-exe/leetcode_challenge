def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set()
  path = bfs(graph, node_A, node_B, visited)
  return path if path != float('inf') else -1
  
  
def build_graph(edges):
  graph = {}
  for e in edges:
    a, b = e
    graph[a] = graph.get(a, [])
    graph[b] = graph.get(b, [])
    graph[a] += [b]
    graph[b] += [a]
  return graph


def bfs(graph, src, dst, visited):
  # bfs iterative
  # queue
  q = [(src, 0)]
  min_path = float('inf')
  while q:
    current = q.pop()
    node, dist = current
    visited.add(node)
    if node == dst:
      min_path = min(min_path, dist)
    for neighbor in graph[node]:
      if not neighbor in visited:
        q = [(neighbor, dist+1)] + q
  return min_path
        
