'''
플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘
따라서 다익스트라 알고리즘처럼 방문하지 않은 노드 중 최단 거리 노드를 찾을 필요가 없다

'''

INF = int(1e9)

def floyd_warshall(node_quantity, vertex_quantity) :
    # 최단 거리 2차원 리스트 생성 및 초기화
    graph = [[INF] * (node_quantity + 1) for _ in range(node_quantity + 1)]
    # 존재하는 간선에 해당하는 거리 리스트 갱신
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for node in range(1, node_quantity + 1) :
        graph[node][node] = 0
    # 간선을 입력받아 길이 초기화
    for vertex in range(vertex_quantity) :
        node_a, node_b, distance = map(int, input().split())
        graph[node_a][node_b] = distance

    # 각 노드를 순회
    for middle in range(1, node_quantity + 1) :
        for right in range(1, node_quantity + 1) :
            for left in range(1, node_quantity + 1):
                graph[left][right] \
                    = min(graph[left][right],
                          graph[left][middle] + graph[middle][right])
            # 해당 노드를 거치는 경로 거리를 확인 및 갱신
