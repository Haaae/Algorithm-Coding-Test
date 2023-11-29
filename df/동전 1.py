
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

counts = [0] * (k + 1) # k = 10일 때, 0 ~ 10
counts[0] = 1

for coin in coins:
    cur_value = coin
    while cur_value <= k:
        counts[cur_value] += counts[cur_value - coin]
        cur_value += 1

print(counts[-1])
