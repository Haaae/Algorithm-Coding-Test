from collections import deque

def print_queue():
    count_document, target_index = map(int, input().split())

    q = deque(map(int, input().split()))
    count_sequence = 0

    while target_index >= 0:

        # 문서가 한개 남았을 경우
        if count_document == 1:
            count_sequence += 1
            target_index -= 1
            continue

        max_priority = max(q)
        first_document = deque.popleft(q)

        # 맨 앞의 문서가 가장 중요도가 높은 문서일 경우
        if first_document >= max_priority:
            count_sequence += 1
            target_index -= 1
            continue

        # 맨 앞의 문서보다 중요도가 높은 문서가 존재할 경우
        if first_document < max_priority:
            deque.append(q, first_document)
            target_index -= 1

            # 맨 앞 문서가 target 문서라면
            if target_index == -1:
                target_index = len(q) - 1
                continue

    print(count_sequence)


count_test_case = int(input())

for _ in range(count_test_case):
    print_queue()
