from collections import deque

def bfs():
    q = deque([[a, 1]])
    while q:
        node, sec = q.popleft()

        if node == b:
            return sec

        for next in [node*2, int(str(node)+"1")]:
            if next <= b:
                q.append([next, sec+1])
    return -1
a, b = map(int, input().split())
print(bfs())
