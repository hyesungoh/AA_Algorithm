# n = int(input())
# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))
# ans = 0
# for _ in range(n):
#     t1, t2 = min(l1), max(l2)
#     ans += t1 * t2
#     l1.remove(t1); l2.remove(t2)
# print(ans)

input()
l1 = map(int, input().split())
l2 = map(int, input().split())
print(sum(map(lambda x, y: x * y, sorted(l1), sorted(l2, reverse=True))))
