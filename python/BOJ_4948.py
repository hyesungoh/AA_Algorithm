def erato(n):
    sieve = [True for _ in range(n+1)]
    sieve[1] = False
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return sieve


l = []
mn = 0
while True:
    n = int(input())
    if not n:
        break
    l.append(n)
    mn = max(mn, n)

sieve = erato(2 * mn)

for i in l:
    print(sieve[i+1:(2*i)+1].count(True))
