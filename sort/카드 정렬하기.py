import heapq

n = int(input())

numbers = [int(input()) for _ in range(n)]

heapq.heapify(numbers)

sums = [heapq.heappop(numbers)]

while len(numbers) >= 2:
    values = [sums[-1], heapq.heappop(numbers), heapq.heappop(numbers)]
    max_value = max(values)
    heapq.heappush(numbers, max_value)
    values.remove(max_value)
    sums.append(sum(values))

if numbers:
    sums.append(numbers.pop() + sums[-1])

print(sum(sums[1:]))