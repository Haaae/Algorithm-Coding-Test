def press(s, length):
    count = 1
    last_str = s[0:length]
    new_s = ''
    for i in range(1, len(s) // length + 1):
        if (i * length) + length > len(s):
            now_str = s[i * length:]
        else:
            now_str = s[i * length:(i * length) + length]
        if now_str == last_str:
            count += 1
            continue

        if count > 1:
            new_s += str(count) + last_str

        if count <= 1:
            new_s += last_str
        count = 1
        last_str = now_str

    if count > 1:
        new_s += str(count) + last_str

    if count <= 1:
        new_s += last_str

    return new_s


def solution(s):
    if len(s) == 0:
        return 0

    strs = []

    for i in range(1, len(s) // 2 + 1):
        strs.append(len(press(s, i)))

    return min(strs)