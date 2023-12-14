
EMPTY = 0
SUDOKU_LEN = 9

sudoku = [list(map(int, input().split())) for _ in range(SUDOKU_LEN)]

empties = []

for x in range(SUDOKU_LEN):
    for y in range(SUDOKU_LEN):
        if sudoku[x][y] == EMPTY:
            empties.append((x, y))


def dfs(index):

    if index == len(empties):
        return True

    x, y = empties[index]

    for i in range(1, 10):

        if check_square(x, y, i) and check_row(i, x) and check_col(i, y):
            sudoku[x][y] = i
            result = dfs(index + 1)

            if result:
                return result

            sudoku[x][y] = EMPTY

    return False


def check_row(i, x):
    return i not in sudoku[x]


def check_col(i, y):

    for line in sudoku:
        if line[y] == i:
            return False
    return True


def check_square(x, y, i):
    nx = (x // 3) * 3
    ny = (y // 3) * 3

    for j in range(3):
        for k in range(3):
            if sudoku[nx + j][ny + k] == i:
                return False

    return True


dfs(0)

for line in sudoku:
    print(*line)
