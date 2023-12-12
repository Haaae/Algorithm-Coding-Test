l, c = map(int, input().split())

chars = sorted(list(input().split()))

stack = []

vowel = {'a', 'e', 'i', 'o', 'u'}


def dfs(n):
    if len(stack) == l:
        count_vowel = len(set(stack).intersection(vowel))
        if count_vowel >= 1 and len(stack) - count_vowel >= 2:
            print(''.join(stack))

        return

    for i in range(n, c):
        stack.append(chars[i])
        dfs(i + 1)
        stack.pop()


dfs(0)
