import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(graph, s): # 그래프와 시작점
    q = []
    heapq.heappush(q, [0, s]) # 리스트 q에 [가중치, 도착지]와 같은 형태로 사용
    dist = [INF for _ in range(len(graph))] # 각 도착지까지의 최소 거리를 저장할 리스트

    while q:
        weight, here = heapq.heappop(q)

        if weight > dist[here]: # 현재 가중치가 저장돼 있는 가중치보다 클 시
            continue

        for there, next_weight in graph[here].items():
            # 그래프는 [{}, {도착지: 가중치, 도착지1: 가중치1}]과 같이 저장
            next = weight + next_weight # 현재 가중치와 그래프에 저장된 가중치를 더함
            dist[there] = min(dist[there], next) # 저장돼 있는 것과 비교하여 저장
            heapq.heappush(q, [next, there]) # 리스트 q에 [다음 가중치, 다음 도착지]를 힙 연산을 통해 넣음
    return dist

n = int(input())
m = int(input())
graph = [{} for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    # 출발지, 도착지가 같을 때 더욱 작은 값을 저장
    if v in graph[u]:
        graph[u][v] = min(w, graph[u][v])
    else:
        graph[u][v] = w

start, end = map(int, input().split())
print(dijkstra(graph, start)[end])
