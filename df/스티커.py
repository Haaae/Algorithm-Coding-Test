t = int(input())


def dp():

    n = int(input())

    up = list(map(int, input().split()))
    down = list(map(int, input().split()))

    if n == 1:
        print(max(up[0], down[0]))
        return
    if n == 2:
        print(max(up[0] + down[1], up[1] + down[0]))
        return

    up[1] += down[0]
    down[1] += up[0]

    for i in range(2, n):
        up[i] += max(down[i - 2], down[i - 1])
        down[i] += max(up[i - 2], up[i - 1])

    print(max(up[-1], down[-1]))


for _ in range(t):
    dp()
