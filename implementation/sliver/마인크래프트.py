# 목표 높이를 위한 블록이 충분한지 확인한다.
## 각 땅의 높이가

n, m, b = map(int, input().split())

ground = []

max_height = 0
total_height = 0
count_area = n * m

for _ in range(n):
    tmp = list(map(int, input().split()))

    total_height += sum(tmp)
    max_height = max(max(tmp), max_height)

    ground.append(tmp)

min_time = 1e9
result_height = 0
for target_height in range(max_height, -1, -1):

    count_need_block = target_height * count_area - total_height - b    # b는 기본적으로 소유한 블록 개수
    if count_need_block > 0:
        continue

    total_time = 0

    for i in range(n):
        for j in range(m):
            current_height = ground[i][j]

            if current_height > target_height:
                total_time += (current_height - target_height) * 2

            if current_height < target_height:
                total_time += target_height - current_height

    if min_time > total_time:
        min_time = total_time
        result_height = target_height
        continue

    if min_time < total_time:
        break

print(min_time, result_height)
