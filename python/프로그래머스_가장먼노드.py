import sys
INF = sys.maxsize
import heapq

def solution(n, vertex):
    def dijkstra():
        q = []
        heapq.heappush(q, [0, 1])

        while q:
            ndist, nnode = heapq.heappop(q)

            if dist[nnode] < ndist:
                continue

            nextDist = ndist + 1
            for nextNode in graph[nnode]:
                if dist[nextNode] > nextDist:
                    dist[nextNode] = nextDist
                    heapq.heappush(q, [nextDist, nextNode])


    graph = {i: [] for i in range(n+1)}
    dist = [INF for _ in range(n+1)]
    dist[1] = 0

    for s, e in vertex:
        graph[s].append(e)
        graph[e].append(s)

    dijkstra()
    max_num, cnt = 0, 1
    for i in range(1, n+1):
        if max_num < dist[i]:
            max_num = dist[i]
            cnt = 1
        elif max_num == dist[i]:
            cnt += 1

    return cnt
