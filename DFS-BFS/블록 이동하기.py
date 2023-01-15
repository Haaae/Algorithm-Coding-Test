WALL = 1
SPACE = 0


def solution(board):
    count = 987654321

    return count_find_location(board, ((0, 0), (0, 1)), count)


def count_find_location(board, locations, count):
    new_count = 0
    location0, location1 = locations
    x0, y0 = location0
    x1, y1 = location1
    if can_move_up(board, locations):
        new_count += 1
        count_find_location(board, ((x0 - 1, y0), (x1 - 1, y1)), count)
        new_count -= 1

    if can_move_down(board, locations):
        new_count += 1
        count_find_location(board, ((x0 + 1, y0), (x1 + 1, y1)), count)
        new_count -= 1

    if can_move_right(board, locations):
        new_count += 1
        count_find_location(board, ((x0, y0 + 1), (x1, y1 + 1)), count)
        new_count -= 1

    if can_move_left(board, locations):
        new_count += 1
        count_find_location(board, ((x0, y0 - 1), (x1, y1 - 1)), count)
        new_count -= 1

    if can_rotate_clock(board, location0, location1):
        new_count += 1
        if is_horizontal(locations):
            if location0[1] < location1[1]:
                count_find_location(board, (location0, ((location0[0] + 1), location0[1])), count)
            else:
                count_find_location(board, (location0, ((location0[0] - 1), location0[1])), count)
        else:
            if location0[0] < location1[0]:
                count_find_location(board, (location0, ((location0[0]), location0[1] - 1)), count)
                # 축이 아래쪽일 때
            else:
                count_find_location(board, (location0, ((location0[0]), location0[1] + 1)), count)
        new_count -= 1

    if can_rotate_clock(board, location1, location0):
        new_count += 1
        if is_horizontal(locations):
            if location1[1] < location0[1]:
                count_find_location(board, (location1, ((location1[0] + 1), location1[1])), count)
            else:
                count_find_location(board, (location1, ((location1[0] - 1), location1[1])), count)
        else:
            if location1[0] < location0[0]:
                count_find_location(board, (location1, ((location1[0]), location1[1] - 1)), count)
                # 축이 아래쪽일 때
            else:
                count_find_location(board, (location1, ((location1[0]), location1[1] + 1)), count)
        new_count -= 1

    if can_rotate_revese_clock(board, location0, location1):
        new_count += 1
        if is_horizontal(locations):
            if location0[1] < location1[1]:
                count_find_location(board, (location0, ((location0[0] - 1), location0[1])), count)
            else:
                count_find_location(board, (location0, ((location0[0] + 1), location0[1])), count)
        else:
            if location0[0] < location1[0]:
                count_find_location(board, (location0, ((location0[0]), location0[1] + 1)), count)
                # 축이 아래쪽일 때
            else:
                count_find_location(board, (location0, ((location0[0]), location0[1] - 1)), count)
        new_count -= 1

    if can_rotate_revese_clock(board, location1, location0):
        new_count += 1
        if is_horizontal(locations):
            if location1[1] < location0[1]:
                count_find_location(board, (location1, ((location1[0] - 1), location1[1])), count)
            else:
                count_find_location(board, (location1, ((location1[0] + 1), location1[1])), count)
        else:
            if location1[0] < location0[0]:
                count_find_location(board, (location1, ((location1[0]), location1[1] + 1)), count)
                # 축이 아래쪽일 때
            else:
                count_find_location(board, (location1, ((location1[0]), location1[1] - 1)), count)
        new_count -= 1

    return min(new_count, count)


def is_horizontal(locations):
    location0, location1 = locations[0], locations[1]
    return location0[0] == location1[0]


def can_move_up(board, locations):
    x0, y0 = locations[0]
    x1, y1 = locations[1]

    return x0 - 1 >= 0 and x1 - 1 >= 0 and board[x0 - 1][y0] == SPACE and board[x1 - 1][y1] == SPACE


def can_move_down(board, locations):
    x0, y0 = locations[0]
    x1, y1 = locations[1]
    n = len(board)
    return x0 + 1 < n and x1 + 1 < n and board[x0 + 1][y0] == SPACE and board[x1 + 1][y1] == SPACE


def can_move_right(board, locations):
    x0, y0 = locations[0]
    x1, y1 = locations[1]
    n = len(board)
    return y0 + 1 < n and y1 + 1 < n and board[x0][y0 + 1] == SPACE and board[x1][y1 + 1] == SPACE


def can_move_left(board, locations):
    x0, y0 = locations[0]
    x1, y1 = locations[1]

    return y0 - 1 >= 0 and y1 - 1 >= 0 and board[x0][y0 - 1] == SPACE and board[x1][y1 - 1] == SPACE


def can_rotate_clock(board, axis, moving):
    lenght = len(board)
    if is_horizontal((axis, moving)):
        # 축이 왼쪽일 때
        if axis[1] < moving[1]:
            return moving[0] + 1 < lenght and axis[0] + 1 < lenght and board[moving[0] + 1][moving[1]] == SPACE and \
                   board[axis[0] + 1][axis[1]] == SPACE
            # 축이 오른쪽일 때
        else:
            return moving[0] - 1 >= 0 and axis[0] - 1 >= 0 and board[moving[0] - 1][moving[1]] == SPACE and \
                   board[axis[0] - 1][axis[1]] == SPACE
    else:  # 수직일 때
        # 축이 위쪽일 때
        if axis[0] < moving[0]:
            return moving[1] - 1 >= 0 and axis[1] - 1 >= 0 and board[moving[0]][moving[1] - 1] == SPACE and \
                   board[axis[0]][axis[1] - 1] == SPACE
            # 축이 아래쪽일 때
        else:
            return moving[1] + 1 < lenght and axis[1] + 1 < lenght and board[moving[0]][moving[1] + 1] == SPACE and \
                   board[axis[0]][axis[1] + 1] == SPACE


def can_rotate_revese_clock(board, axis, moving):
    lenght = len(board)
    if is_horizontal((axis, moving)):  # 수평일 때
        # 축이 왼쪽일 때
        if axis[1] < moving[1]:
            return moving[0] - 1 >= 0 and axis[0] - 1 >= 0 and board[moving[0] - 1][moving[1]] == SPACE and \
                   board[axis[0] - 1][axis[1]] == SPACE
            # 축이 오른쪽일 때
        else:
            return moving[0] + 1 < lenght and axis[0] + 1 < lenght and board[moving[0] + 1][moving[1]] == SPACE and \
                   board[axis[0] + 1][axis[1]] == SPACE
    else:  # 수직일 때
        # 축이 위쪽일 때
        if axis[0] < moving[0]:
            return moving[1] + 1 < lenght and axis[1] + 1 < lenght and board[moving[0]][moving[1] + 1] == SPACE and \
                   board[axis[0]][axis[1] + 1] == SPACE
            # 축이 아래쪽일 때
        else:
            return moving[1] - 1 >= 0 and axis[1] - 1 >= 0 and board[moving[0]][moving[1] - 1] == SPACE and \
                   board[axis[0]][axis[1] - 1] == SPACE