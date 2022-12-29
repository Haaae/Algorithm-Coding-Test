# 크루스칼 알고리즘, Kruskal Algorithm
'''
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 가선이 사이클을 발생시키는지 확인한다.
    a. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    b. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.
'''


# 특정 원소가 속한 집합을 찾기. 경로 압축 기법 적용
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루튼 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    if b < a:
        parent[a] = b

# 크루스칼 알고리즘
def union_find(node, vertex_amount):
    parent = [0] * (node + 1)  # 부모 테이블 초기화

    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    for i in range(1, node + 1):
        parent[i] = i

    # 간선을 담을 리스트 선언
    vertexs = []

    # 각 간선을 입력받음
    for i in range(vertex_amount):
        a, b, cost = map(int, input().split())
        vertexs.append((cost, a, b))

    # 간선을 거리 순으로 정렬
    vertexs.sort()

    # 최소 신장 트리의 간선 값 합
    result = 0

    # 모든 간선에 대한 최소 신장 트리 포함 여부 결정
    for vertex in vertexs :
        cost, a, b = vertex
        if parent[a] == parent[b]:
            continue
        union_parent(parent, a, b)
        result += cost
    return result


def print_result(result):
    print(result)