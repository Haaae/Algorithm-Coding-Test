from collections import deque


INF = 1e9


n = int(input())

m = int(input())

costs = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())

    costs[start].append((end, cost))



def bfs(start):

    total_costs = [(INF, i) for i in range(n + 1)]

    total_costs[start] = (0, start)

    queue = deque()
    queue.append((start, 0))

    while queue:
        current, record_distance = queue.popleft()

        current_total_cost, before = total_costs[current]

        if current_total_cost < record_distance:
            continue

        for next, next_cost in costs[current]:
            next_total_cost, _ = total_costs[next]

            tmp_cost = next_cost + current_total_cost
            if tmp_cost < next_total_cost:
                total_costs[next] = (tmp_cost, current)
                queue.append((next, tmp_cost))

    return total_costs


start, end = map(int, input().split())
total_costs = bfs(start)

city = end
routes = deque()
routes.append(end)

while city != start:
    _, before = total_costs[city]
    routes.appendleft(before)
    city = before


print(total_costs[end][0])
print(len(routes))
print(*routes)

