
from collections import deque

INF = 1e9

n, k = map(int, input().split())


def bfs(start, target):
    distances_size = target + start + 1
    distances = [INF] * distances_size

    distances[start] = 0

    queue = deque()
    queue.append((start, 0))

    while queue:
        current, value = queue.popleft()

        current_distance = distances[current]
        if current_distance < value:
            continue

        if current * 2 < distances_size and current_distance < distances[current * 2]:
            distances[current * 2] = current_distance
            queue.append((current * 2, current_distance))

        if current + 1 < distances_size and current_distance + 1 < distances[current + 1]:
            distances[current + 1] = current_distance + 1
            queue.append((current + 1, current_distance + 1))

        if current - 1 >= 0 and current_distance + 1 < distances[current - 1]:
            distances[current - 1] = current_distance + 1
            queue.append((current - 1, current_distance + 1))

    return distances


print(bfs(n, k)[k])
