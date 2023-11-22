n, m = map(int, input().split())
arr = []
def dfs(start):
    if len(arr) == m:
        print(*arr, end=" ")
        print()
        return

    for i in range(start, n + 1):
        arr.append(i)
        dfs(i + 1)
        arr.pop()

dfs(1)
