import sys
from collections import deque
input = sys.stdin.readline

def left(s):
    n = int(s)
    return set_format(int(n % 1000 * 10 + n / 1000))

def right(s):
    n = int(s)
    return set_format(int(n % 10 * 1000 + n // 10))

def double(s):
    t = int(s)
    t = (t*2) % 10000
    return str(set_format(t))

def minus(s):
    if s == "0000":
        return "9999"
    t = "0000" + str(int(s)-1)
    l = len(t)
    return t[l-4:l]

def set_format(s):
    t = "0000" + str(s)
    l = len(t)
    return t[l - 4:l]

def check(s, e):
    q = deque()
    q.append([s, ""])
    visit = [False for _ in range(10001)]
    visit[int(s)] = True

    while q:
        now, cnt = q.popleft()
        if now == e:
            return cnt

        t = double(now)
        if not visit[int(t)]:
            q.append([t, cnt + "D"])
            visit[int(t)] = True

        t = minus(now)
        if not visit[int(t)]:
            q.append([t, cnt + "S"])
            visit[int(t)] = True

        t = left(now)
        if not visit[int(t)]:
            q.append([t, cnt + "L"])
            visit[int(t)] = True

        t = right(now)
        if not visit[int(t)]:
            q.append([t, cnt + "R"])
            visit[int(t)] = True

for _ in range(int(input())):
    s, e = map(set_format, input().split())
    print(check(s, e))
