n = int(input())


def can_attack(new_position, queen_position, distance):
    return new_position == queen_position or distance == abs(new_position - queen_position) # 대각선 검증


def dfs(target_count_queen, positions):

    current_count_queen = len(positions)
    numbers_of_case = 0

    if current_count_queen == target_count_queen:
        return 1

    # 새로운 퀸 위치 후보
    for new_queen in range(target_count_queen):
        can_add = True
        # 기존 퀸 위치와 비교
        for i in range(current_count_queen):

            if can_attack(new_queen, positions[i], current_count_queen - i):
                can_add = False
                break

        if can_add:
            positions.append(new_queen)
            numbers_of_case += dfs(target_count_queen, positions)
            positions.pop()

    return numbers_of_case


print(dfs(n, []))
