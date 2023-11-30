
n = int(input())

a, b, c = map(int, input().split())

min_arr = [a, b, c]
max_arr = [a, b, c]

for _ in range(n - 1):
    next = list(map(int, input().split()))
    min_arr = [next[0] + min(min_arr[0], min_arr[1]), next[1] + min(min_arr), next[2] + min(min_arr[1], min_arr[2])]
    max_arr = [next[0] + max(max_arr[0], max_arr[1]), next[1] + max(max_arr), next[2] + max(max_arr[1], max_arr[2])]

print(max(max_arr), end=' ')
print(min(min_arr))
