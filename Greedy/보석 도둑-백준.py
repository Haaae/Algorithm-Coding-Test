import sys
import heapq

WEIGHT = 0
VALUE = 1
MIN_GEM = 0

n, k = map(int, sys.stdin.readline().split())

gems = []
for _ in range(n):
    m, v = tuple(map(int, sys.stdin.readline().split()))
    heapq.heappush(gems, (m, v))

bags = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
bags.sort()

result = 0
tmp_gems = []

for bag in bags:
    while gems and bag >= gems[MIN_GEM][WEIGHT]:
        # 현재 가방에 들어갈 수 있는 보석은 모두 tmp_gems에 추가. 최대 heap
        heapq.heappush(tmp_gems, -heapq.heappop(gems)[VALUE])
    if tmp_gems:
        # 이때 최대 가치 보석을 제외한 모든 보석은 tmp_gems에 남아있음
        # 남아있는 모든 보석은 이후의 가방에 들어갈 수 있는 무게이므로(가방의 가용무게는 오름차순)
        # 이후의 heappop() 연산을 통해 우선순위가 정해진다.
        result -= heapq.heappop(tmp_gems)
    elif not gems:
        break

print(result)
