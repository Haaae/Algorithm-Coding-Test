from collections import deque

MIN = 0

n = int(input())

vertices = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    root, child, weight = map(int, input().split())
    vertices[root].append((child, weight))
    vertices[child].append((root, weight))


def bfs(start):
    global vertices, n

    distances = [MIN] * (n + 1)

    queue = deque()
    queue.append(start)

    while queue:
        current_node = queue.popleft()
        current_distance = distances[current_node]

        for next, weight in vertices[current_node]:
            temp = current_distance + weight

            if next != start and distances[next] == MIN:
                distances[next] = temp
                queue.append(next)

    return distances


distances = bfs(1)
i = distances.index(
    max(distances)
)
result = bfs(i)
print(max(result))
