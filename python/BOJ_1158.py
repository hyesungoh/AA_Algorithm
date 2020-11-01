n, k = map(int, input().split())
n_l = list(range(1, n+1))
l = []
i = 0

while len(l) != n:
    i = (i + (k-1)) % len(n_l)
    l.append(str(n_l.pop(i)))
print("<%s>"%', '.join(l))
