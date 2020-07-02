# d = dict(); input()
# for i in input().split():
#     if i not in d.keys():
#         d[i] = 1
#     else:
#         print(i)
#         break

from sys import stdin
def read():
    while 1:
        s = stdin.read(100000)
        if not s: return
        while s[-1] != ' ':
            extra = stdin.read(1)
            if not extra: break
            s+= extra
        yield from map(int, s.split())

n = int(input())
ans = n * (n-1) // 2 - sum(read())
print(-ans)
