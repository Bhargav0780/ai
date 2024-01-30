from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            queue.extend(graph[current_node] - visited)

# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'}
}

# Starting from node 'A'
print("BFS starting from node B:")
bfs(graph, 'B')
