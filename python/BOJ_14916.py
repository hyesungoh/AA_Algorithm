n = int(input())
for i in range(n // 5, -1, -1):
    temp = n - (5 * i)
    if temp % 2 == 0:
        print(i + temp // 2)
        exit(0)
print(-1)
