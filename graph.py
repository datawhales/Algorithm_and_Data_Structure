# adjacency matrix
INF = 99999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# adjacency list
graph = [[] for _ in range(3)]
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)