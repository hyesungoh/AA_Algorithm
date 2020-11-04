s, ans = 0, 0
for _ in range(10):
    n = int(input())
    if abs(100 - s) >= abs(100 - s - n):
        ans = s + n
    s += n
print(ans)
