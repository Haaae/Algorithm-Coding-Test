n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split());
max_result = - int(1e9)
min_result = int(1e9)


def dfs(sum, idx):
    global max_result, min_result, add, sub, mul, div

    if idx == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return

    if add:  # 0은 if문에서 False 취급. add != 0과 동일
        add -= 1
        dfs(sum + number[idx], idx + 1)
        add += 1
    if sub:
        sub -= 1
        dfs(sum - number[idx], idx + 1)
        sub += 1
    if mul:
        mul -= 1
        dfs(sum * number[idx], idx + 1)
        mul += 1
    if div:
        div -= 1
        dfs(int(sum / number[idx]), idx + 1)
        div += 1


dfs(number[0], 1)

print(max_result)
print(min_result)