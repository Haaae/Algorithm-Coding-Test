
count_man, count_relation = map(int, input().split())

relations = [[] for _ in range(count_man)]

for _ in range(count_relation):
    m1, m2 = map(int, input().split())
    relations[m1].append(m2)
    relations[m2].append(m1)


def dfs(stack):
    if len(stack) == 5:
        return True

    for friend in relations[stack[-1]]:
        if friend not in stack:
            stack.append(friend)
            result = dfs(stack)
            stack.pop()

            if result:
                return result

    return False


stack = []

result = False

for man in range(count_man):
    stack.append(man)
    result = dfs(stack)

    if result:
        break

    stack.pop()

print(1 if result else 0)


