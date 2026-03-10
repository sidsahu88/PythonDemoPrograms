
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print('Visited:', start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A'],
        'C': ['A', 'F'],
        'D': ['A', 'E', 'F'],
        'E': ['D'],
        'F': ['C', 'D']
    }

    dfs_recursive(graph, 'A')
