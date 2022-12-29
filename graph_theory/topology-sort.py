'''
위상 정렬 알고리즘은 방향 그래프에서만 사용 가능
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    a. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을그래프에서 제거한다.
    b. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
'''

from collections import deque

def topology_sort_setup(node_amount, vertex_amount) :
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (vertex_amount + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(node_amount + 1)]

    # 방향 그래프의 모든 간선 정보를 입력받기
    for _ in range(vertex_amount) :
        a, b = map(int, input().split())
        graph[a].append(b)  # 정점 a에서 b로 이동 가능
        # 진입 차수 1 증가
        indegree[b] += 1

    topology_sort(indegree, graph)

# 위상 정렬 함수
def topology_sort(indegree, graph) :
    result = [] # 알고리즘 수행 결과를 담을 리스트
    queue = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음에 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(indegree) :
        if indegree[i] == 0 :
            queue.append(i)

    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 원소 꺼내기
        node = queue.popleft()
        result.append(node)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[node] :
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0 :
                queue.append(i)

        for i in result :
            print(i, end=' ')