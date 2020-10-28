# import heapq
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize
#
# def dijkstra(k, graph):
#     dist = [INF for _ in range(len(graph))]
#     q = []
#     heapq.heappush(q, [0, k, k])
#     weight = 0
#     while q:
#         weight, here, start = heapq.heappop(q)
#         if start == k:
#             dist[here] = min(dist[here], weight)
#         else:
#             dist[here] = min(dist[here], weight + dist[start])
#
#         for there, distance in graph[here].items():
#             heapq.heappush(q, [distance, there, here])
#
#     return dist
#
#
# v, e = map(int, input().split())
# graph = [{} for _ in range(v+1)]
# k = int(input())
# for _ in range(e):
#     u, v, w = map(int, input().split())
#     if v in graph[u]:
#         graph[u][v] = min(w, graph[u][v])
#     else:
#         graph[u][v] = w
#
# dist = dijkstra(k, graph)
# for i in dist[1:]:
#     print(i if i != INF else 'INF')


import heapq # 거리가 짧은 순으로 계산해야하기 때문에 힙 사용
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(k, graph):
    # 노드의 수 + 1 만큼 최대 크기로 이루어진 거리를 저장할 리스트
    dist = [INF for _ in range(len(graph))]
    # 시작 노드의 거리는 0으로
    dist[k] = 0

    q = []
    # 거리, 행선지 순으로 리스트에 힙 연산으로 push
    heapq.heappush(q, [0, k])
    while q:
        # 거리 weight, 행선지 here을 힙 연산으로 pop
        weight, here = heapq.heappop(q)

        # graph[행선지] = {도착지: 거리} 순으로 저장돼 있음
        for there, distance in graph[here].items():
            # 다음 간선까지 길이는 현재 길이 + 저장된 거리
            next_dist = distance + weight

            # 현재 dist에 저장된 거리보다 작을 시
            if dist[there] > next_dist:
                # 저장 후 [거리, 행선지]를 리스트에 힙 연산으로 push
                dist[there] = next_dist
                heapq.heappush(q, [next_dist, there])

    return dist


v, e = map(int, input().split())
# graph[출발지] = {도착지: 거리, 도착지1: 거리1}
graph = [{} for _ in range(v+1)]
k = int(input())
for _ in range(e):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(w, graph[u][v])
    else:
        graph[u][v] = w

dist = dijkstra(k, graph)
for i in dist[1:]:
    print(i if i != INF else 'INF')
