import heapq

INF = 1e9


def dijkstra(graph, n, start):
    distances = [INF] * (n + 1)
    distances[start] = 0

    queue = [start]
    heapq.heapify(queue)

    while queue:
        node = heapq.heappop(queue)

        for next, distance in graph[node]:
            temp = distances[node] + distance
            if temp < distances[next]:
                distances[next] = temp
                heapq.heappush(queue, next)

    return distances


n, e = map(int, input().split())

graph = [[] for _ in range((n + 1))]

for _ in range(e):
    node1, node2, distance = map(int, input().split())
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))

v1, v2 = map(int, input().split())

distances_start = dijkstra(graph, n, 1)
distances_v1 = dijkstra(graph, n, v1)
distances_v2 = dijkstra(graph, n, v2)

result = min(
    distances_start[v1] + distances_v1[v2] + distances_v2[n],
    distances_start[v2] + distances_v2[v1] + distances_v1[n]
)

print(result if result < INF else -1)
