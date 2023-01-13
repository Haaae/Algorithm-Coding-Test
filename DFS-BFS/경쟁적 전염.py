from collections import deque

SPACE = 0

n, k = map(int, input().split())

virus_map = [list(map(int, input().split())) for _ in range(n)]

second, target_x, target_y = map(int, input().split())

viruses = []

for i in range(n) :
    for j in range(n) :
        if virus_map[i][j] != SPACE :
            viruses.append((virus_map[i][j], 0, i, j))

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

viruses.sort()
q = deque(viruses)
while q :
    virus, s, x, y = q.popleft()
    if s == second :
        break

    for i in range(len(dx)) :
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]

        if tmp_x < n and tmp_y < n and tmp_x >= 0 and tmp_y >= 0 :
            if virus_map[tmp_x][tmp_y] == SPACE :
                virus_map[tmp_x][tmp_y] = virus
                q.append((virus, s + 1, tmp_x, tmp_y))

print(virus_map[target_x - 1][target_y - 1])