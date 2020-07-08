import sys
input=sys.stdin.readline

class Queue:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, n):
        self.len += 1
        self.list.append(n)

    def pop(self):
        if self.len > 0:
            self.len -= 1
            return self.list.pop(0)
        else: return -1

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def front(self):
        return -1 if self.len == 0 else self.list[0]

    def back(self):
        return -1 if self.len == 0 else self.list[self.len-1]

q = Queue()
for _ in range(int(input())):
    s = input().strip()
    if 'push' in s: q.push(s.split()[1])
    elif s == 'pop': print(q.pop())
    elif s == 'size': print(q.size())
    elif s == 'empty': print(q.empty())
    elif s == 'front': print(q.front())
    elif s == 'back': print(q.back())
    else: print('none')
