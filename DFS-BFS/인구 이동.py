def required_population_movement(world_map, l, r):
    length = len(world_map)
    result = []
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    for x in range(length):
        for y in range(length):
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > -1 and ny > -1 and nx < length and ny < length:
                    population_sub = abs(world_map[x][y] - world_map[nx][ny])
                    if l <= population_sub and population_sub <= r:
                        if (nx, ny) not in result:
                            result.append((nx, ny))
                        if (x, y) not in result:
                            result.append((x, y))

    return result


n, l, r = map(int, input().split())

world_map = [list(map(int, input().split())) for _ in range(n)]

count = 0

contries = required_population_movement(world_map, l, r)

while contries:
    count += 1

    while contries:
        queue = []
        queue.append(contries.pop(0))
        connected_contries = []
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        while queue:
            x, y = queue.pop()
            connected_contries.append((x, y))
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) in contries:
                    contries.remove((nx, ny))
                    queue.append((nx, ny))

        population_sum = 0
        for contry in connected_contries:
            x, y = contry
            population_sum += world_map[x][y]
        population_per_contry = population_sum // len(connected_contries)
        for contry in connected_contries:
            x, y = contry
            world_map[x][y] = population_per_contry

    contries = required_population_movement(world_map, l, r)
print(count)