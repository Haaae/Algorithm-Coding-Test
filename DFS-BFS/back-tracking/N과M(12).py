n, m = map(int, input().split())

numbers = list(set(map(int, input().split())))
numbers.sort()

arr = []


def dfs(i, numbers_len):
    if len(arr) == m:
        print(*arr, end=" ")
        print()
        return

    for j in range(i, numbers_len):
        arr.append(numbers[j])
        dfs(j, numbers_len)
        arr.pop()



dfs(0, len(numbers))
