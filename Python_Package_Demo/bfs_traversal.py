def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)
            print('Visited:', node)
            queue.extend(graph.get(node))


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A'],
        'C': ['A', 'F'],
        'D': ['A', 'E', 'F'],
        'E': ['D'],
        'F': ['C', 'D']
    }

    bfs(graph, 'A')