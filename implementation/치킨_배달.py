from itertools import combinations

HOUSE = 1
CHICKEN = 2

n, maximum_chicken = map(int, input().split())

chicken_map = [list(map(int, input().split())) for _ in range(n)]


def calculation_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

# 모든 치킨집 위치 확인
# 모든 집 위치 확인
houses = []
chickens = []
chicken_distances = []
for i in range(n):
    for j in range(n):
        element = chicken_map[i][j]
        if element == HOUSE:
            houses.append((i, j))

        if element == CHICKEN:
            chickens.append((i, j))

candidates = list(combinations(chickens, maximum_chicken))

answer = 987654321
for candidate in candidates:
    sum = 0
    for house in houses:
        distance = 987654321
        for chicken in candidate:
            new = calculation_distance(house, chicken)
            if new < distance:
                distance = new

            if new == 1:
                break
        sum += distance

    if sum < answer:
        answer = sum

print(answer)
