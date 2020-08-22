# s = 0
# for _ in range(int(input())):
#     s += int(input())
# if s == 0: print(0)
# else:
#     print('+' if s > 0 else '-')


import sys
ip = sys.stdin.readline
for i in range(3):
    s = 0
    for _ in range(int(ip())):
        s += int(ip())
    print(('0' if s == 0 else '-' if s < 0 else '+'))
