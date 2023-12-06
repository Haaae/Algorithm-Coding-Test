INF = 1e9

count_city, count_vertex = map(int, input().split())

graph = [[] for _ in range(count_city + 1)]

for _ in range(count_vertex):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def bfs():
    distances = [INF] * (count_city + 1)
    distances[1] = 0

    is_exist_negative_circle = False

    for _ in range(count_city - 1):
        for current in range(1, count_city + 1):
            for neighbor, weight in graph[current]:
                if neighbor == 1 or distances[current] == INF:
                    continue
                if distances[current] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current] + weight

    for current in range(1, count_city + 1):
        for neighbor, weight in graph[current]:
            if distances[current] + weight < distances[neighbor]:
                if distances[current] == INF:
                    continue
                is_exist_negative_circle = True

    return distances[1:], is_exist_negative_circle


distances, is_exist_negative_circle = bfs()

if is_exist_negative_circle:
    print(-1)

if not is_exist_negative_circle:
    for distance in distances[1:]:
        print(distance if distance != INF else -1)
