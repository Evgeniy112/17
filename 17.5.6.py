graph = {
    'A': ['B','C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
dfs('A', graph, 'A')