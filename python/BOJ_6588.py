import sys
input = sys.stdin.readline

def get_prime(n):
    sieve = [True for _ in range(n+1)]
    sieve[1] = False
    mn = int(n ** 0.5)

    for i in range(1, mn+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return sieve

def goldbach(n):
    n1, n2 = 0, 0
    for i in range(2, (n // 2) + 1):
        if prime[i] and prime[n-i]:
            n1, n2 = i, n-i
            return "%d = %d + %d" %(n, n1, n2)
    return "Goldbach's conjecture is wrong."

l = []
while True:
    n = int(input())
    if n == 0:
        break
    l.append(n)

prime = get_prime(max(l))

for n in l:
    print(goldbach(n))
