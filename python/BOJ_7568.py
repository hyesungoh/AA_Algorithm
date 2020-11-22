n = int(input())
l = []
rank = [0 for _ in range(n)]

for _ in range(n):
    l.append(list(map(int, input().split())))

for i in range(n):
    now_w, now_h = l[i][0], l[i][1]
    r = 1
    for j in range(n):
        com_w, com_h = l[j][0], l[j][1]
        if now_w < com_w and now_h < com_h:
            r += 1
    rank[i] = r

[print(i, end=" ") for i in rank]
