import sys
input = sys.stdin.readline

def cal(n, m):
    if n <= m:
        return m - n
    else:
        return m + 26 - n

for _ in range(int(input())):
    l1, l2 = input().split()
    print('Distances: ', end='')
    for i in range(len(l1)):
        print(cal(ord(l1[i]), ord(l2[i])), end=' ')
    print()
