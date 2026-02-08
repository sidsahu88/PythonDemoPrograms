
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print('Visited:', node)
            stack.extend(reversed(graph.get(node)))


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A'],
        'C': ['A', 'F'],
        'D': ['A', 'E', 'F'],
        'E': ['D'],
        'F': ['C', 'D']
    }

    dfs_iterative(graph, 'A')
