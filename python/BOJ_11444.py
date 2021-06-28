# n = int(input())
# x, y = 0, 1
# for _ in range(n):
#     x, y = y, (x+y) % 1000000007
# print(x)


def power(adj, n):
    if n == 1: return adj
    elif n % 2: return multi(power(adj, n-1), adj)
    else: return power(multi(adj, adj), n // 2)


def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum_n = 0
            for k in range(2):
                sum_n += a[i][k] * b[k][j]
            temp[i][j] = sum_n % MOD

    return temp


MOD = 1000000007
adj = [[1, 1], [1, 0]]
start = [[1], [1]]
N = int(input())

print(1 if N < 3 else multi(power(adj, N-2), start)[0][0])
