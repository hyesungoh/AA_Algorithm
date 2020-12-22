def erato(n, k):
    l = [False for _ in range(0, n+1)]
    cnt = 0
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if not l[j]:
                l[j] = True
                cnt += 1
                if cnt == k:
                    return j


n, k = map(int, input().split())
print(erato(n, k))
