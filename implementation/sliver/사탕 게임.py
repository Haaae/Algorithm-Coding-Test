# 각 사탕의 위치를 하나씩 바꾼다.
# 사탕을 바꿨을 때 가장 많이 먹을 수 있는 사탕의 개수를 구한다.
## 한 줄의 시작 사탕 종류를 a라고 할 때, a가 아닐 때까지 count up 한다.
## a가 아니게 되면 max_line_count = max(max_line_count, count) 한 후, count = 0 한다.
## 줄의 끝까지 반복한다.
## 한 줄이 끝나면, max_count = max(max_count, max_line_count)한다.
## 결과를 반환한다.
# 최대값을 출력한다.

RED = 'C'
YELLOW = 'Y'
BLUE = 'P'
GREEN = 'Z'


def max_continuous_candy(n, candy_graph):
    result = 0

    # 가로줄
    for i in range(n):

        max_count = 0
        count = 1
        previous_candy = candy_graph[i][0]

        for j in range(1, n):
            current_candy = candy_graph[i][j]

            if current_candy == previous_candy:
                count += 1
            else:
                previous_candy = current_candy
                max_count = max(max_count, count)
                count = 1

        result = max(result, max_count, count)

    # 세로줄
    for j in range(n):
        max_count = 0
        count = 1
        previous_candy = candy_graph[0][j]
        for i in range(1, n):
            current_candy = candy_graph[i][j]

            if current_candy == previous_candy:
                count += 1
            else:
                previous_candy = current_candy
                max_count = max(max_count, count)
                count = 1

        result = max(result, max_count, count)

    return result


n = int(input())

candy_graph = [list(input()) for _ in range(n)]

dx = [0, 1]
dy = [1, 0]

result = max_continuous_candy(n, candy_graph) # 위치 변경없는 상태가 최장길이일 수도 있음

isOver = False
for i in range(n):
    for j in range(n):

        for d in range(len(dx)):
            x = i + dx[d]
            y = j + dy[d]

            if x >= n or y >= n:
                continue

            candy_graph[i][j], candy_graph[x][y] = candy_graph[x][y], candy_graph[i][j]
            result = max(result, max_continuous_candy(n, candy_graph))
            candy_graph[i][j], candy_graph[x][y] = candy_graph[x][y], candy_graph[i][j]

            if result == n:
                isOver = True
                break

        if isOver:
            break

    if isOver:
        break


print(result)
