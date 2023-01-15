def isBalanced(string):
    return string.count('(') == string.count(')')


def isPerfect(string):
    if string[0] == ')':
        return False

    stack = []

    for i in range(len(string)):
        if stack:
            if stack[len(stack) - 1] == string[i]:
                stack.append(string[i])
                continue
            stack.pop()
    return not stack  # 리스트는 비어있으면 False로 취급


def splitString(string):
    for i in range(1, len(string) + 1):
        u, v = string[0:i], string[i:]
        if i == len(string):
            v = ''
        if isBalanced(u):
            return u, v


def turnString(string):
    result = ""
    for i in range(len(string)):
        if string[i] == '(':
            result += ')'
        else:
            result += '('
    return result


def solution(p):
    if p == '':
        return p

    u, v = splitString(p)

    if isPerfect(u):
        return u + solution(v)

    return '(' + solution(v) + ')' + turnString(u[1:-1])