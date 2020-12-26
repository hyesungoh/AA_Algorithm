def bt(depth, temp_list):
    if sum(temp_list) == s and temp_list != []:
        ans[0] += 1

    elif depth == n:
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            temp_list.append(l[i])

            bt(depth+1, temp_list)

            temp_list.pop()
            for j in range(i+1, n):
                visit[j] = False


n, s = map(int, input().split())
l = list(map(int, input().split()))
visit = [False for _ in range(n)]
tl = []
ans = [0]
bt(0, tl)
print(ans[0])
