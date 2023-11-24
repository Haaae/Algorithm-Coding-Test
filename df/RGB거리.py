RED = 0
GREEN = 1
BLUE = 2

n = int(input())

result = list(map(int, input().split()))

for _ in range(n - 1):
    before_red, before_green, before_blue, = result[RED], result[GREEN], result[BLUE]

    rgb = list(map(int, input().split()))

    result[RED] = rgb[RED] + min(before_green, before_blue)
    result[GREEN] = rgb[GREEN] + min(before_red, before_blue)
    result[BLUE] = rgb[BLUE] + min(before_red, before_green)

print(min(result))
