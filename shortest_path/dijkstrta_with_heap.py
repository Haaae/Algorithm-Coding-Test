import heapq

'''
다익스트라 알고리즘은 특정 노드에서 다른 노드들로 가는 최단경로를 찾는 알고리즘
- 방문한 노드 체크 및 노드 거리를 나타내기 위한 노드길이(n)만큼의 리스트 두 개 선언
- 시작 노드부터 시작하여 각 노드와 연결되어 있는 노드를 거치며 거리 리스트를 갱신
'''

INF = int(1e9)
DISTANCE = 1
NODE = 0

def dijkstra(graph, start_node, node_quantity) :
    distance = [INF] * node_quantity
    q = []
    visited = [False] * node_quantity

    # 시작 노드에 대해서 초기화
    setup(start_node, distance, q)

    while q : # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        # 최단 거리가 가장 짧은 거리인 노드를 뽑아야만 정상적인 갱신이 가능
        now_distance, now_node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now_node] < now_distance :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node_distance in graph[now_node] :
            cost = now_distance + node_distance[DISTANCE]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node_distance[NODE]] :
                distance[node_distance[NODE]] = cost
                heapq.heappush(q, (cost, node_distance[NODE]))

def setup(node, distance, q) :
    heapq.heappush(q, (0, node))  # (거리, 노드)
    distance[node] = 0