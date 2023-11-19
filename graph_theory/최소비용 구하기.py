
import heapq

INF = 1e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, distance = map(int, input().split())
    graph[start].append((end, distance))


def dijkstra(graph, start):
    distances = [INF] * len(graph)
    distances[start] = 0
    queue = [(start, 0)]

    while queue:
        current, current_distance = heapq.heappop(queue)

        if distances[current] < current_distance:
            continue

        for next, distance in graph[current]:
            temp = distances[current] + distance
            if temp < distances[next]:
                distances[next] = temp
                heapq.heappush(queue, (next, distances[next]))

    return distances


start, end = map(int, input().split())

print(
    dijkstra(graph, start)[end]
)
