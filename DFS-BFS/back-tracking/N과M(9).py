n, m = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

arr = []
results = set()


def dfs(i, numbers):
    if len(arr) == m:
        results.add(tuple(arr))
        return

    arr.append(numbers[i])

    new_numbers = numbers[0:i] + numbers[i + 1:]
    for j in range(len(new_numbers)):
        dfs(j, new_numbers)
    if not new_numbers:
        dfs(i, new_numbers)

    arr.pop()


for i in range(len(numbers)):
    dfs(i, numbers)

for result in sorted(list(results)):
    print(*result, end=" ")
    print()
