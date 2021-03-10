# def dijkstra():
#     price4dist = [INF for _ in range(N+1)]
#     # price4dist[1] = 0
#
#     q = []
#     heapq.heappush(q, [0, 1])
#
#     while q:
#         cnt, now = heapq.heappop(q)
#         if cnt > price4dist[now]:
#             continue
#
#         for next, next_dist in graph[now]:
#             next_price = (next_dist * price[now]) + cnt
#
#             if price4dist[next] >= next_price:
#                 if price[next] > price[now]:
#                     price[next] = price[now]
#
#                 price4dist[next] = next_price
#                 heapq.heappush(q, [next_price, next])
#
#     return price4dist

import sys
import heapq
INF = sys.maxsize

def dijkstra():
    # 현재 위치, 현재까지 가장 싼 기름값
    result = [[INF for _ in range(2501)] for _ in range(N+1)]

    q = []
    # 총 비용, 현재까지 가장 싼 주유소, 현재 위치
    heapq.heappush(q, [0, price[1], 1])

    while q:
        node = heapq.heappop(q)
        here_cost = node[0]
        here_min_oil = node[1]
        here = node[2]

        # 저장된 값이 현재 값보다 클 시
        if here_cost > result[here][here_min_oil]:
            continue

        # 목적지에 도착 시
        if here == N:
            return here_cost

        for there, dist in graph[here]:
            # 현재까지 가장 싼 주유소에서 기름을 넣은 것으로 계산
            there_cost = here_cost + (dist * here_min_oil)
            # 가장 싼 주유소 갱신
            there_min_oil = min(here_min_oil, price[there])

            # 현재 저장된 값보다 갱신될 값이 작을 시
            if result[there][there_min_oil] > there_cost:
                result[there][there_min_oil] = there_cost
                heapq.heappush(q, [there_cost, there_min_oil, there])
    return -1


N, M = map(int, input().split())
price = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(N+1)}

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

print(dijkstra())
