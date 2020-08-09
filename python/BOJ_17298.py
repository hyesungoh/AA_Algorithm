# n = int(input())
# l = list(map(int, input().split()))
# for i in range(n):
#     for j in range(i, n):
#         if l[j] > l[i]:
#             print(l[j], end=' ')
#             break
#         elif j == n-1:
#             print(-1, end=' ')

class Stk:
    def __init__(self):
        self.list = []
        self.len = 0
        self.init_len = []
    def push(self, n, i):
        self.list.append(n)
        self.len += 1
        self.init_len.append(i)
    def top(self):
        return self.list[-1]
    def del_top(self):
        self.list.pop(-1)
        self.len -= 1
        self.init_len.pop(-1)

n = int(input())
s = list(map(int, input().split()))
ans_l = [-1] * n
stk = Stk()
for i in range(n-1):

    while stk.len > 0 and s[i+1] > stk.top():
        ans_l[stk.init_len[-1]] = s[i+1]
        stk.del_top()
    if s[i] < s[i+1]:
        ans_l[i] = s[i+1]
    else:
        stk.push(s[i], i)

print(*ans_l, end=' ')

# n=int(input())
# a=[*map(int,input().split())]
# s=[]; nge=[-1]*n
# for i in range(n):
#   while s and a[s[-1]]<a[i]:
#     nge[s.pop()]=a[i]
#   s.append(i)
# print(*nge)
