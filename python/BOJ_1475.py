from math import ceil

l = [0 for _ in range(10)]
n = list(map(int, input()))

for i in n:
    if i == 9:
        l[6] += 1
        continue
    l[i] += 1

l[6] = ceil(l[6] / 2)
print(max(l))
