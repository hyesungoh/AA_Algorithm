n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    for j in range(i, n):
        if l[j] > l[i]:
            print(l[j], end=' ')
            break
        elif j == n-1:
            print(-1, end=' ')
