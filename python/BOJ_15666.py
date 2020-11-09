def bt(depth, index):
    if depth == m:
        print(*ans)
        return

    temp = 0
    for i in l:
        if index <= i and temp != i:
            temp = i
            ans.append(i)
            bt(depth+1, i)

            ans.pop()

n, m = map(int, input().split())
l = sorted(map(int, input().split()))
ans = []

bt(0, 0)
