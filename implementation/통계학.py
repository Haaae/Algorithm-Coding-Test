import math

n = int(input())

numbers: list[int] = [int(input()) for _ in range(n)]

numbers.sort()

count_numbers = len(numbers)

# 산술평균
raw_value = sum(numbers) / count_numbers
preprocessing_value = raw_value + 0.5 if raw_value > 0 else raw_value - 0.5

print(math.floor(raw_value + 0.5))

# 중앙값
print(numbers[count_numbers // 2])

# 최빈값

frequency_dict = dict()

for number in numbers:
    if number in frequency_dict:
        frequency_dict[number] += 1
    else:
        frequency_dict[number] = 1

sorted_frequency = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)


print(sorted_frequency[0][0] if count_numbers == 1 or sorted_frequency[0][1] != sorted_frequency[1][1] else sorted_frequency[1][0])

# 범위
print(numbers[-1] - numbers[0])
