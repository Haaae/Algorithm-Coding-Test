from collections import deque

INF = 1e9
EMPTY = 0
BABY_SHARK = 9


def can_not_move_through_space(baby_size, graph, nx, ny):
    return graph[nx][ny] > baby_size


def is_not_shortest_distance(cur_distance, distance):
    return cur_distance + 1 > distance


def is_invalid_range(nx, ny):
    return nx < 0 or ny < 0 or nx >= n or ny >= n


n = int(input())

graph = [
    list(
        map(int, input().split())
    )
    for _ in range(n)
]

eat_count = 0
baby_size = 2
total_distance = 0
coordinate_baby = ()

for i in range(n):
    for j in range(n):
        if graph[i][j] == BABY_SHARK:
            coordinate_baby = (i, j)

# 아기 상어의 위치를 기준으로 bfs를 시작한다.
# 이때 이동할 수 있는 위치에 먹이가 있다면 해당 먹이까지의 거리를 기존 먹이와의 거리와 비교한다.
# 만약 거리가 같다면 가장 왼쪽, 위쪽에 있는 먹이를 선택한다.
# 만약 거리가 다르다면 거리가 짧은 먹이를 선택한다.
# 만약 거리가 다른데, 후에 찾은 먹이의 거리가 더 길다면 탐색을 중지하고 이전에 찾은 먹이를 먹으러 이동한다.
# 이동 시 아기 상어의 몸집을 계산하고, 위치를 갱신한다.

def bfs():
    global graph, coordinate_baby, eat_count, baby_size

    visited = [[False] * n for _ in range(n)]

    x, y = coordinate_baby
    visited[x][y] = True
    queue = deque()
    queue.append((x, y, 0))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    distance = INF
    coordinate_prey = (INF, INF)

    while queue:
        cur_x, cur_y, cur_distance = queue.popleft()

        for i in range(4):
            nx = dx[i] + cur_x
            ny = dy[i] + cur_y

            if (
                    is_invalid_range(nx, ny) or
                    visited[nx][ny] or
                    can_not_move_through_space(baby_size, graph, nx, ny)
            ):
                continue

            visited[nx][ny] = True

            if graph[nx][ny] < baby_size and graph[nx][ny] != EMPTY:
                if is_not_shortest_distance(cur_distance, distance):
                    queue.clear()
                    break


                coordinate_prey = min(coordinate_prey, (nx, ny))
                distance = cur_distance + 1

            queue.append((nx, ny, cur_distance + 1))

    return distance != INF, distance, coordinate_prey

while True:
    is_moved, distance, coordinate_prey = bfs()

    if not is_moved:
        break

    total_distance += distance

    graph[coordinate_baby[0]][coordinate_baby[1]] = EMPTY

    x, y = coordinate_prey

    coordinate_baby = (x, y)
    graph[x][y] = BABY_SHARK

    eat_count += 1
    if eat_count == baby_size:
        baby_size += 1
        eat_count = 0

print(total_distance)
