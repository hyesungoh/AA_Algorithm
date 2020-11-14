import sys
input = sys.stdin.readline

n = int(input())
d = {}
se = set()
for _ in range(n):
    s = input()[0]
    if s in d:
        d[s] += 1
        if d[s] >= 5:
            se.add(s)
    else:
        d[s] = 1

print("PREDAJA" if len(se) == 0 else ''.join(sorted(se)))
