import sys

#recursion error 방지
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def print_tree(arr):
    if not arr:
        return

    root = arr[0]

    length = len(arr)
    index = length
    for i in range(1, length):
        if arr[i] > root:
            index = i
            break

    print_tree(arr[1:index])
    print_tree(arr[index:])

    print(root)


print_tree(arr)
