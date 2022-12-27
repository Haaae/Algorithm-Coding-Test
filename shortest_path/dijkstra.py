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
    visited = [False] * node_quantity

    # 시작 노드에 대해서 초기화
    setup(start_node, graph, distance, visited)

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(node_quantity - 1) :
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        smallest_node = get_smallest_node(distance, visited, node_quantity)
        visited[smallest_node] = True
        # 현재 노드와 연결된 다른 노드 확인 및 갱신
        renewal_distance(smallest_node, graph, distance)

def setup(node, graph, distance, visited) :
    distance[node] = 0
    visited[node] = True
    for node_distance in graph[node]:
        # i는 start node와 연결된 노드를 나타내는 튜플(연결 노드, 거리)
        distance[node_distance[NODE]] = node_distance[DISTANCE]  # 연결된 노드의 거리를 갱신


def renewal_distance(node, graph, distance) :
    for node_distance in graph[node]:
        cost = distance[node] + node_distance[DISTANCE]
        if cost < distance[node_distance[NODE]]:
            distance[node_distance[NODE]] = cost

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node(distance, visited, node_quantity) :
    min_value = INF
    index = 0
    for i in range(1, node_quantity + 1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index