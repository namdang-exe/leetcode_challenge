def breathFirstSearch(graph, source):
    # bfs iteratively
    # use queue - first in first out
    q = [source]
    while q:
        current = q.pop()
        print(current)
        q = graph[current] + q


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

breathFirstSearch(graph, 'a')
