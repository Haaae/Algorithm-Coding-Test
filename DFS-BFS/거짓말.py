# 진실을 아는 사람이 속한 모든 집단의 사람은 진실을 아는 사람이 된다
# 진실을 아는 사람이 속한 모임의 사람을 모두 set에 넣는다
# set의 값을 하나 꺼내어 모든 모임을 순회하며 값이 속한 모임을 찾는다.
    # 값이 속한 모임은 거짓말 모임에서 제외되며, 해당 모임의 사람과 set의 사람을 union한다.
# 모든 set의 값을 순회한 후 거짓말 모임 개수를 센다.


def parse_input():
    _info = list(map(int, input().split()))
    return _info[0], set(_info[1:])


counts = list(map(int, input().split()))

count_guest = counts[0]
count_party = counts[1]

count_knowing, knowings = parse_input()

parties = []
for _ in range(count_party):
    _, people = parse_input()
    parties.append(set(people))


checked = set()

while knowings:
    know = knowings.pop()
    checked.add(know)

    checked_parties = []
    while parties:
        party = parties.pop()
        if know in party:
            for guest in party:
                if guest not in checked:
                    knowings.add(guest)
        else:
            checked_parties.append(party)

    parties = checked_parties


    ## 이터레이터로 반복할 경우 컬렉션의 요소가 변경되면 예상치 못한 결과가 나타난다.
    # for party in parties:
    #     if know in party:
    #         for guest in party:
    #             if guest not in checked:
    #                 knowings.add(guest)
    #         parties.remove(party)

print(len(parties))