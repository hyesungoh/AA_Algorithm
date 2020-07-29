n = int(input())
for i in range(n):
    t = sum(map(int,str(i)))
    if i + t == n:
        print(i)
        exit(0)
print(0)
