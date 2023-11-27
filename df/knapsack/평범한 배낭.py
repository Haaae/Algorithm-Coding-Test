n, k = map(int, input().split())

knapsack = [[0] * (k + 1) for _ in range(n + 1)]

stuff = [(0, 0)]

for _ in range(n):
    weight, value = map(int, input().split())
    stuff.append((weight, value))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight, value = stuff[i]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
            continue

        knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j])

print(knapsack[-1][-1])

