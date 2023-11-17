import sys

REVERSE = "R"
DELETE = "D"


def calculate(p_arr, numbers):
    reverse_count = 0
    start = 0
    end = len(numbers)
    is_error = False

    for p in p_arr:
        if p == REVERSE:
            reverse_count += 1
            continue

        if p == DELETE:
            if is_reversed(reverse_count):
                end -= 1
            else:
                start += 1

            if end - start < 0:
                is_error = True

    if is_error:
        print("error")
    elif is_reversed(reverse_count):
        print_result(reversed(numbers[start:end]))
    else:
        print_result(numbers[start:end])


def is_reversed(reverse_count):
    return reverse_count % 2 == 1


def print_result(result):
    print("[", end="")
    print(*result, sep=",", end="")
    print("]")


t = int(input())

for _ in range(t):
    p_arr = input()
    n = int(input())

    numbers_input = input()[1:-1]
    numbers = []
    if numbers_input:
        numbers = list(
            map(
                int,
                numbers_input.split(",")
            )
        )
    calculate(p_arr, numbers)
