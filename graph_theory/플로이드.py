INF = 1e9

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    start, end, distance = map(int, input().split())
    graph[start][end] = min(graph[start][end], distance)

for middle in range(n + 1):
    for start in range(n + 1):
        for end in range(n + 1):
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

for starts in graph[1:]:
    for distance in starts[1:]:
        print(distance if distance < INF else 0, end=" ")
    print()