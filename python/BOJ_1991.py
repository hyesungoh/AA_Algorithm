import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def front(root, graph):
    if root in graph:
        l, r = graph[root]
        print(root, end='')
        front(l, graph)
        front(r, graph)
    else: return

def middle(root, graph):
    if root in graph:
        l, r = graph[root]
        middle(l, graph)
        print(root, end='')
        middle(r, graph)
    else: return

def last(root, graph):
    if root in graph:
        l, r = graph[root]
        last(l, graph)
        last(r, graph)
        print(root, end='')
    else: return


graph = {}
for _ in range(int(input())):
    d, l, r = input().split()
    graph[d] = [l, r]


front('A', graph)
print()
middle('A', graph)
print()
last('A', graph)
