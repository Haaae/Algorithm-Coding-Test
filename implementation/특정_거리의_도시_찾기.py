total_city, total_road, target_distance, start_city = map(int, input().split())

city_map = [[] for _ in range(total_city + 1)]
distance_from_start = [987654321] * (total_city + 1)
distance_from_start[start_city] = 0

for _ in range(total_road):
    start, end = map(int, input().split())
    city_map[start].append(end)

queue = [start_city]

answer = []
while queue:
    node = queue.pop(0)

    if distance_from_start[node] >= target_distance:
        break

    for next_node in city_map[node]:
        if distance_from_start[next_node] != 987654321:
            continue

        if distance_from_start[next_node] > distance_from_start[node] + 1:
            distance_from_start[next_node] = distance_from_start[node] + 1
            queue.append(next_node)
            if distance_from_start[next_node] == target_distance:
                answer.append(next_node)
                continue

if len(answer) == 0:
    print(-1)
else:
    for x in sorted(answer):
        print(x)

