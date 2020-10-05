import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    l.append(list(map(int, input().split())))
l = sorted(l, key=lambda x: (x[1], x[0]))

ans = 0
start_time = 0
for i in l:
    if start_time <= i[0]:
        ans += 1
        start_time = i[1]

print(ans)
