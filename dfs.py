def depthFirstSearch(graph, source):
    # dfs iterative
    # go all the way down one path
    # use stack - last in first out
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        neighbors = graph[current]
        stack += neighbors

def depthFirstSearchII(graph, source):
    # dfs recursive
    # don't need to use stack
    # don't need base cases because when algo gets to a node is null (no neighbor), it terminates
    print(source)
    for neighbor in graph[source]:
        depthFirstSearchII(graph, neighbor)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

# depthFirstSearch(graph, 'a')
depthFirstSearchII(graph, 'a')
