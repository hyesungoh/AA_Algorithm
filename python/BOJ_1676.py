def f(n):
    return n * f(n-1) if n > 1 else 1

n = f(int(input()))
ans = 0
for i in reversed(str(n)):
    if i == '0': ans += 1
    else: break
print(ans)

# n = int(input()) // 5
# print(n + n // 5 + n // 25)
