import sys
input = sys.stdin.readline

n = int(input())
l = [0]
ans = []
max_num = 0

for _ in range(n):
    tn = int(input())

    if max_num < tn:
        for i in range(max_num + 1, tn):
            l.append(i)
            ans.append('+')
        ans.append('+')
        ans.append('-')
        max_num = tn
    else:
        if l[-1] == tn:
            l.pop()
            ans.append('-')
        else:
            print("NO")
            exit(0)

[print(i) for i in ans]
