# import sys
# input = sys.stdin.readline
#
# def dijkstra(graph, d):
#     total = [i for i in range(d+1)]
#     count = 0
#     value = 0
#     while count <= d:
#         if count in graph:
#             for short in graph[count]:
#                 total[short[0]] = min(total[short[0]], short[1] + total[count])
#         else:
#             value = min(total[count], value)
#             total[count] = value
#
#         value += 1
#         count += 1
#     return total
#
# n, d = map(int, input().split())
# graph = {}
# for _ in range(n):
#     u, v, w = map(int, input().split())
#     if d >= v and v-u > w: # 지름길을 이용할 필요가 없을 때
#         if u in graph:
#             graph[u].append([v, w])
#         else:
#             graph[u] = [[v, w]]
#
# total = dijkstra(graph, d)
# print(total[d])

import sys
input = sys.stdin.readline

def dp(graph, d):
    l = [i for i in range(10000)]
    count = 0
    value = 0
    while count <= d:
        if value in graph:
            for short_cut in graph[value]:
                l[short_cut[0]] = min(l[short_cut[0]], short_cut[1] + l[value])

        l[value+1] = min(l[value+1], l[value]+1)
        value += 1
        count += 1
    return l

n, d = map(int, input().split())
graph = {}
for _ in range(n):
    u, v, w = map(int, input().split())
    if d >= v and v - u > w:
        if u in graph:
            graph[u].append([v, w])
        else:
            graph[u] = [[v, w]]

l = dp(graph, d)
print(l[d])
