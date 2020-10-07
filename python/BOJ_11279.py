from bisect import insort
import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    s = int(input())
    if s > 0:
        insort(l, s)
    else:
        if l == []:
            print('0')
        else:
            print(l.pop())
