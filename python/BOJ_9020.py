def get_prime(n):
    sieve = [True for _ in range(n+1)]
    sieve[1] = False
    mn = int(n ** 0.5)

    for i in range(1, mn+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return sieve

l = []
for _ in range(int(input())):
    l.append(int(input()))

ans = []
prime = get_prime(max(l))

for n in l:
    n1, n2 = 0, 0
    for i in range(2, (n//2)+1):
        if prime[i] and prime[n-i]:
            n1, n2 = i, n-i
    print(n1, n2)
