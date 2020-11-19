def erato():
    sieve = [True for _ in range(m+1)]
    sieve[1] = False
    max_n = int(m ** 0.5)
    for i in range(2, max_n+1):
        if sieve[i]:
            for j in range(i+i, m+1, i):
                sieve[j] = False
    return sieve

n = int(input())
m = int(input())
ans = 0
min_n = False
prime_list = erato()

for i in range(n, m+1):
    if prime_list[i]:
        ans += i
        if not min_n:
            min_n = i

print(("%d\n%d" %(ans, min_n)) if ans != 0 else -1)
