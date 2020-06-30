import sys
input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.len = 0
        self.list = []
    def push(self, n):
        self.len += 1
        self.list.append(n)
    def pop(self):
        if self.len == 0:
            return -1
        self.len -= 1
        return self.list.pop()
    def size(self):
        return self.len
    def empty(self):
        return 1 if self.len == 0 else 0
    def top(self):
        return self.list[-1] if self.len != 0 else -1

s = Stack()
for _ in range(int(input())):
    t = input().strip()
    if 'push' in t:
        num = list(t.split())[1]
        s.push(num)
    elif t == "pop": print(s.pop())
    elif t == 'size': print(s.size())
    elif t == 'empty': print(s.empty())
    elif t == 'top': print(s.top())
    else: print('none')
