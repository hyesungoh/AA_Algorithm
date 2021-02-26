import sys
input = sys.stdin.readline

i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break

    vp = v // p
    ans = vp * l
    ans += (v - vp * p) if l > (v - vp * p) else l

    print("Case %d: %d" %(i, ans))
    i += 1
