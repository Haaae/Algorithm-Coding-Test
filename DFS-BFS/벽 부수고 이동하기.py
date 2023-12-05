from collections import deque

EMPTY = 0
WALL = 1
NOT_BREAK = 0
BREAK = 1
INF = 1e9

n, m = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(n)]


def bfs():

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    distances = [[[INF] * m for _ in range(n)] for _ in range(2)]

    distances[NOT_BREAK][0][0] = 1
    queue = deque()
    queue.append((0, 0, NOT_BREAK, 1))

    while queue:
        x, y, break_wall_status, previous_distance = queue.popleft()

        if previous_distance < distances[break_wall_status][x][y]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == EMPTY and previous_distance + 1 < distances[break_wall_status][nx][ny]:
                distances[break_wall_status][nx][ny] = previous_distance + 1
                queue.append((nx, ny, break_wall_status, distances[break_wall_status][nx][ny]))

            if (
                    graph[nx][ny] == WALL and
                    break_wall_status == NOT_BREAK and
                    previous_distance + 1 < distances[break_wall_status][nx][ny]
            ):
                distances[BREAK][nx][ny] = previous_distance + 1
                queue.append((nx, ny, BREAK, distances[BREAK][nx][ny]))

    return min(distances[BREAK][-1][-1], distances[NOT_BREAK][-1][-1])


result = bfs()
print(result if result != INF else -1)
