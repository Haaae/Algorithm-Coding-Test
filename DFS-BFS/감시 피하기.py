from itertools import combinations
import copy


def canCatchStudent(teacher, tmp_map):
    x, y = teacher
    nx, ny = x, y
    possible = True
    while nx + 1 < n:
        nx += 1
        if tmp_map[nx][ny] == STUDENT:
            possible = False
            break
        if tmp_map[nx][ny] == WALL:
            break

    nx, ny = x, y
    while ny + 1 < n:
        ny += 1
        if tmp_map[nx][ny] == STUDENT:
            possible = False
            break
        if tmp_map[nx][ny] == WALL:
            break

    nx, ny = x, y
    while nx - 1 >= 0:
        nx -= 1
        if tmp_map[nx][ny] == STUDENT:
            possible = False
            break
        if tmp_map[nx][ny] == WALL:
            break

    nx, ny = x, y
    while ny - 1 >= 0:
        ny -= 1
        if tmp_map[nx][ny] == STUDENT:
            possible = False
            break
        if tmp_map[nx][ny] == WALL:
            break
    return possible


EMPTY = 'X'
STUDENT = 'S'
TEACHER = 'T'
WALL = 'O'

n = int(input())

school_map = [input().split() for _ in range(n)]

empty_spaces = []
teachers = []
for i in range(n):
    for j in range(n):
        if school_map[i][j] == EMPTY:
            empty_spaces.append((i, j))
        if school_map[i][j] == TEACHER:
            teachers.append((i, j))
printYes = False
location_combinations = list(combinations(empty_spaces, 3))
for location_combination in location_combinations:
    possible = True
    tmp_map = copy.deepcopy(school_map)

    for location in location_combination:
        tmp_map[location[0]][location[1]] = WALL

    for teacher in teachers:
        if not canCatchStudent(teacher, tmp_map):
            possible = False
            break
    if possible:
        print('YES')
        printYes = True
        break

if not printYes:
    print('NO')
