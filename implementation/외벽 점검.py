from itertools import combinations
from itertools import permutations


def canPatral(patrolmans, i, weak_distances):
    for _ in range(i):
        weak_distances.pop()

    for patrolman in patrolmans:
        patrolman = list(patrolman)
        now = patrolman.pop(0)
        success = True
        for distance in weak_distances:
            if now < distance:
                if len(patrolman) == 0:
                    success = False
                    break
                now = patrolman.pop(0)
                continue

            now = now - distance

        if success:
            return True
    return False


def solution(n, weaks, distance):
    answer = -1

    weak_distances = []
    for weak in weaks:
        i = weaks.index(weak)
        if weaks.index(weak) == len(weaks) - 1:
            weak_distances.append(n - weak + weaks[0])
            break

        weak_distances.append(weaks[weaks.index(weak) + 1] - weak)

    # 외벽 점검 숫자 1부터 len(distance)만큼 경우의 수를 통해 가능한지 확인한다.
    for i in range(1, len(distance) + 1):
        patrolmans = list(permutations(distance, i))
        # 만약 가능하다면 곧바로 return한다.
        if canPatral(patrolmans, i, sorted(weak_distances)):
            answer = i
            break

    return answer


print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))