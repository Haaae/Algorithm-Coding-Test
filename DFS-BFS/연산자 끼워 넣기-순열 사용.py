from itertools import permutations


def addIfEquals(operators, index, operator_index, operator_amount):
    for i in range(operator_amount):
        operators.append(operator_index)


ADD = 0
SUB = 1
MULTIPLE = 2
DIVISION = 3

n = int(input())

numbers = list(map(int, input().split()))
operators_amount = list(map(int, input().split()))
operators = []
for i in range(len(operators_amount)):
    if i == ADD:
        addIfEquals(operators, i, ADD, operators_amount[i])
    if i == SUB:
        addIfEquals(operators, i, SUB, operators_amount[i])
    if i == MULTIPLE:
        addIfEquals(operators, i, MULTIPLE, operators_amount[i])
    if i == DIVISION:
        addIfEquals(operators, i, DIVISION, operators_amount[i])

min_result = 987654321
max_result = -90000000

for random_operators in permutations(operators, len(operators)):
    value = numbers[0]
    for i in range(len(random_operators)):
        if random_operators[i] == ADD:
            value += numbers[i + 1]
        if random_operators[i] == SUB:
            value -= numbers[i + 1]
        if random_operators[i] == MULTIPLE:
            value *= numbers[i + 1]
        if random_operators[i] == DIVISION:
            if value == 0:
                continue
            if value < 0:
                value = int((-1 * value // numbers[i + 1]) * -1)
                continue
            value = (value // numbers[i + 1])

    max_result = max(max_result, value)
    min_result = min(min_result, value)

print(max_result)
print(min_result)