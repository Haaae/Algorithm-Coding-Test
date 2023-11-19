import heapq

INF = 1e9

n, d = map(int, input().split())

graph = [[] for _ in range(d + 1)]

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, end, distance, = map(int, input().split())
    if end > d:
        continue
    graph[start].append((end, distance))


def dijkstra(graph, start):
    distances = [INF] * (len(graph))
    distances[start] = 0
    queue = [start]

    while queue:
        node = heapq.heappop(queue)

        for next, distance in graph[node]:
            temp = distances[node] + distance
            if temp < distances[next]:
                distances[next] = temp
                heapq.heappush(queue, next)

    return distances

print(
    dijkstra(graph, 0)[d]
)
