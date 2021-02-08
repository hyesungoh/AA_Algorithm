import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
for i in range(n):
    t = int(input())
    positive.append(t) if t > 0 else negative.append(t)

positive.sort(reverse=True)
negative.sort()
lp = len(positive)
ln = len(negative)

ans = 0
for i in range(0, lp, 2):
    t = positive[i] if i+1 >= lp else positive[i] + positive[i+1] if positive[i] == 1 or positive[i+1] == 1 else positive[i] * positive[i+1]
    ans += t

for i in range(0, ln, 2):
    ans += negative[i] if i+1 >= ln else negative[i] * negative[i+1]

print(ans)
