INF = 1e9

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

counts = [INF] * (k + 1)
counts[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        counts[i] = min(counts[i], counts[i - coin] + 1)

print(counts[-1] if counts[-1] != INF else -1)
