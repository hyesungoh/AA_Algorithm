n, m = map(int, input().split())
s = n*m
for i in input().split():
    print(int(i) - s, end=" ")
