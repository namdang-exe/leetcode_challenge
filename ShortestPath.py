def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set()
  return bfs(graph, node_A, node_B, visited)
  
  
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
  # Don't need a min tracker because wherever it touches first is the shortest one
  q = [(src, 0)]
  while q:
    current = q.pop()
    node, dist = current
    visited.add(node)
    if node == dst:
      return dist
    for neighbor in graph[node]:
      if not neighbor in visited:
        q = [(neighbor, dist+1)] + q
  return -1
        
    
