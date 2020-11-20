def erato():
    sieve = [True for _ in range(m+1)]
    sieve[1] = False
    max_n = int(m ** 0.5)

    for i in range(2, max_n+1):
        if sieve[i]:
            for j in range(i+i, m+1, i):
                sieve[j] = False

    return sieve


n, m = map(int, input().split())
l = erato()
for i in range(n, m+1):
    if l[i]:
        print(i)
