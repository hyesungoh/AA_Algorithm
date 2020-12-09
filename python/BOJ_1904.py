l = [1, 2]
n = int(input())
for i in range(2, n):
    l.append((l[i-2] + l[i-1])%15746)
print(l[n-1])
