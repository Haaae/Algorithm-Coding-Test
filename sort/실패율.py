def solution(N, stages):
    answer = []
    length = len(stages)

    for stage in range(1, N + 1):
        number_of_challenger = stages.count(stage)

        if length == 0:
            fail_rate = 0
        else:
            fail_rate = number_of_challenger / length
            length -= number_of_challenger

        answer.append([fail_rate, stage])

    answer.sort(key=lambda x: (-x[0], x[1]))

    return [i[1] for i in answer]