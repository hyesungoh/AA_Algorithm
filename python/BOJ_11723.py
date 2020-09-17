import sys
input = sys.stdin.readline

class Set:
    def __init__(self):
        self.list = [0] * 21

    def check(self, t):
        t = t.split()
        if t[0] == 'add':
            self.list[int(t[1])] = 1
        elif t[0] == 'remove':
            self.list[int(t[1])] = 0
        elif t[0] == 'check':
            print(self.list[int(t[1])])
        elif t[0] == 'toggle':
            self.list[int(t[1])] = int(not int(self.list[int(t[1])]))
        elif t[0] == 'empty':
            self.list = [0] * 20
        elif t[0] == 'all':
            self.list = [1] * 20

s = Set()
for _ in range(int(input())):
    s.check(input())
