# n = int(input())
# l = sorted(map(int, input().split()))
# ans = 0
# for i in range(n+1):
#     ans += sum(l[0:i])
# print(ans)

input()
ans, t = 0, 0
for i in sorted(map(int, input().split())):
    t += i
    ans += t
print(ans)
