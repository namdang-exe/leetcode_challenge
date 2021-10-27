def hasPath(graph, src, dst):
    # dfs - traverse to the end of the path
    # stack/ recursive
    if src == dst:
        return True
    else:
        # graph[src] is an array of neighbors
        # so we loop through the neighbors
        for neighbor in graph[src]:
            if hasPath(graph, neighbor, dst):
                return True
        return False


def hasPathBfs(graph, src, dst):
    # bfs
    # queue
    q = [src]
    while q:
        current = q.pop()
        if current == dst:
            return True
        q = graph[current] + q
    return False
