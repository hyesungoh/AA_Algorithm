import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
l = [0 for _ in range(n)]
graph = {}
for _ in range(n-1):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

def fp(n):
    for i in graph[n]:
        if l[i - 1] == 0:
            l[i - 1] = n
            fp(i)
fp(1)
[print(i) for i in l[1:]]
