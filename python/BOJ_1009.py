l = [[10], [1], [6,2,4,8], [1,3,9,7], [6,4], [5], [6], [1,7,9,3], [6,8,4,2], [1,9]]
for _ in range(int(input())):
    n, m = map(int, input().split())
    n %= 10
    m %= len(l[n])
    print(l[n][m])
