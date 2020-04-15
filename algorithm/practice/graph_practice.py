def bfs(graph, param):
    queue = [param]
    result = []

    while queue:
        el = queue.pop(0)
        result.append(el)
        child = graph.get(el, None)
        if child:
            queue.extend(child)
    print(result)


def dfs(graph, param):
    stack = [param]
    result = []

    while stack:
        el = stack.pop()
        result.append(el)
        child = graph.get(el, None)
        if child:
            stack.extend(child)
    print(result)


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'D': ['F']
    }

    bfs(graph, 'A')
    dfs(graph, 'A')