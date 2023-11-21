from collections import deque

NOTING = 0
CHEESE = 1
NOT_VISITED = 0
VISITED = 1
NEXT = 2

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def is_empty():
    global graph, n, m, NOTING, CHEESE, NOT_VISITED, VISITED, NEXT

    visited = [[NOT_VISITED for _ in range(m)] for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((0, 0))

    next_disappear_cheese = set()

    while queue:
        x, y = queue.popleft()

        # 이미 방문한 공간
        if visited[x][y] == VISITED:
            continue

        visited[x][y] = VISITED

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 유효하지 않은 범위라면
            if nx < 0 or ny < 0 or n <= nx or m <= ny:
                continue

            value = graph[nx][ny]

            # 빈 공간이고 방문하지 않았다면 다음 목적지 목록에 추가
            if visited[nx][ny] == NOT_VISITED and value == NOTING:
                queue.append((nx, ny))

            # 치즈라면 다음에 없어질 치즈인지 확인
            if value == CHEESE:
                if visited[nx][ny] < NEXT:
                    visited[nx][ny] += 1

                    # 공기와 2면 이상 접촉하면 다음에 없어짐 목록에 추가
                    if visited[nx][ny] == NEXT:
                        next_disappear_cheese.add((nx, ny))

    # 없어지는 치즈 갱신
    for x, y in next_disappear_cheese:
        graph[x][y] = NOTING

    return False if next_disappear_cheese else True


count = 0
while not is_empty():
    count += 1

print(count)
