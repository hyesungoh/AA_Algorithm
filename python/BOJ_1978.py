def erato(n):
    m = int(n ** 0.5)
    sieve = [True for _ in range(n+1)]
    sieve[1] = False

    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return sieve

input()
l = list(map(int, input().split()))
max_n = max(l)
prime_l = erato(max_n)
ans = 0
for i in l:
    if prime_l[i]:
        ans += 1
print(ans)
