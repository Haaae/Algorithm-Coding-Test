# 특정 원소가 속한 집합을 찾기. 경로 압축 기법 적용
def find_parent(parent, x) :
    # 루트 노드가 아니라면, 루튼 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] is not x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    if b < a :
        parent[a] = b

# 서로소 집합 알고리즘
def union_find(node, vertex) :
    parent = [0] * (node + 1) # 부모 테이블 초기화

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, node + 1) :
        parent[i] = i

    # union 연산을 각각 수행
    for i in range(vertex) :
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    return parent

def print_union(vertex, parent) :
    for i in range(1, vertex + 1) :
        print(find_parent(parent, i), end=' ')