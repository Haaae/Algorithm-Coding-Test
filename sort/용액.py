def get_result(solutions, count_solution):
    pointer_small, pointer_big = 0, count_solution - 1
    mmin = 1e10  # 두 용액값의 합의 절대값 중 최소값을 의미하는 변수
    result_solutions = [0, 0]

    while pointer_small < pointer_big:
        solution_small, solution_big = solutions[pointer_small], solutions[pointer_big]

        mmin = update_result(
            mmin,
            result_solutions,
            solution_small,
            solution_big
        )

        pointer_small, pointer_big = update_pointers(
            pointer_small,
            pointer_big,
            solution_small + solution_big
        )

    return result_solutions


def update_result(mmin, result_solutions, solution_small, solution_big):
    abs_sum_solutions = abs(solution_small + solution_big)

    if abs_sum_solutions < mmin:
        result_solutions[0], result_solutions[1] = solution_small, solution_big
        return abs_sum_solutions

    return mmin


def update_pointers(pointer_small, pointer_big, sum_solution):
    # 용액의 합이 0이라면 즉시 종료해야 하므로 while문 조건을 불만족시키도록 포인터 값을 뒤바꾼다.
    if sum_solution == 0:
        pointer_small, pointer_big = pointer_big, pointer_small

    if sum_solution > 0:
        pointer_big -= 1

    if sum_solution < 0:
        pointer_small += 1

    return pointer_small, pointer_big


def main():
    count_solution = int(input())

    solutions = list(map(int, input().split()))
    solutions.sort()

    print(
        *get_result(
            solutions,
            count_solution
        )
    )


if __name__ == "__main__":
    main()
