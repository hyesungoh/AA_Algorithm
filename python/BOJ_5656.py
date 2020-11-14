import sys
input = sys.stdin.readline
i = 1
while True:
    n1, oper, n2 = input().split()
    if oper == 'E':
        break
    print("Case %s: " %i, end="")
    s = str(eval(n1 + oper + n2)).lower()
    print(s)
    i += 1
