def gcm(x, y):
    n = max(x, y)
    d = min(x, y)

    while (n % d) != 0:
        t = n % d
        n = d
        d = t

    return d
input()
n = eval(input().replace(' ', '*'))
input()
m = eval(input().replace(' ', '*'))
ans = str(gcm(n, m))
l = len(ans)
print(ans) if l < 9 else print(ans[l - 9 : l + 1])
