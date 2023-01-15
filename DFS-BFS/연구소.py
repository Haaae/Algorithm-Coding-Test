from itertools import combinations
import copy

SPACE = 0
WALL = 1
VIRUS = 2

n, m = map(int, input().split())

lab_map = []

for _ in range(n):
    lab_map.append(list(map(int, input().split())))

# 빈 벽의 위치와 개수를 모두 확인
# 모든 바이러스의 위치와 개수 확인
number_space = 0
spaces = []
viruses = []

for i in range(n):
    for j in range(m):
        if lab_map[i][j] == VIRUS:
            viruses.append((i, j))
            continue
        if lab_map[i][j] == SPACE:
            number_space += 1
            spaces.append((i, j))

# 3개 벽을 세우는 모든 경우의 수 반복
x_plus = [1, 0, 0, -1]
y_plus = [0, 1, -1, 0]
answer = 0
for random_spaces in combinations(spaces, 3):
    simulation_map = copy.deepcopy(lab_map)
    for random_space in random_spaces:
        i, j = random_space
        simulation_map[i][j] = WALL

    stack = copy.deepcopy(viruses)

    # 각 경우 중 바이러스와 연결된 빈 방을 바이러스로 바꿈

    convert_count = 0
    while stack:
        x, y = stack.pop()
        for i in range(0, 4):
            tmp_x = x + x_plus[i]
            tmp_y = y + y_plus[i]
            if tmp_x >= n or tmp_y >= m or tmp_x < 0 or tmp_y < 0:
                continue
            if simulation_map[tmp_x][tmp_y] == SPACE:
                simulation_map[tmp_x][tmp_y] = VIRUS
                stack.append((tmp_x, tmp_y))
                convert_count += 1

    # 최대 빈 방 개수 갱신
    # print(convert_count)
    # print(answer)
    answer = max(answer, number_space - convert_count - 3)

print(answer)
