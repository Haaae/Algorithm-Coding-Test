import heapq

MIN = -1

v = int(input())

vertices = [[] for _ in range(v + 1)]

for _ in range(v):
    inputs = list(map(int, input().split()))
    vertex = inputs[0]
    for i in range(1, len(inputs) - 1, 2):
        vertices[vertex].append((inputs[i], inputs[i + 1]))


def reverse_dijkstra(start):
    distances = [MIN] * len(vertices)
    distances[start] = 0
    queue = [(start, 0, start)]

    while queue:
        current_node, current_distance, previous_node = heapq.heappop(queue)

        if current_distance < distances[current_node]:
            continue

        for next_node, distance in vertices[current_node]:
            if next_node == previous_node:
                continue

            temp = distances[current_node] + distance
            if temp > distances[next_node]:
                distances[next_node] = temp
                heapq.heappush(queue, (next_node, temp, current_node))

    return distances


distances = reverse_dijkstra(1)
print(
    max(
        reverse_dijkstra(
            distances.index(
                max(distances))
        )
    )
)
