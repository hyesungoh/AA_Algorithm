cl = [1, 1, 2, 2, 2, 8]
nl = list(map(int, input().split()))
for i in range(6):
    print(cl[i] - nl[i], end=' ')
