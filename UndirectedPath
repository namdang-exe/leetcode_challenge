def undirected_path(edges, src, dst):
  # construct neighbor graph
  graph = build_graph(edges)
  visited = ()
  return has_path(graph, src, dst, visited)  
  
  
def build_graph(edges):
  graph = {}
  for e in edges:
    a,b = e
    graph[a] = graph.get(a, [])
    graph[b] = graph.get(b, [])
    graph[a] += [b]
    graph[b] += [a]
  return graph


def has_path(graph, src, dst, visited):
  # dfs 
  # recursive
  if src in visited:
    return False
  if src == dst:
    return True
  visited += (src,)
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited):
      return True
  return False
