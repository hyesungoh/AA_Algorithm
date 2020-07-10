import sys
input=sys.stdin.readline
class Deque:
    def __init__(self):
        self.len = 0
        self.list = [];

    def push_front(self, n):
        self.len += 1
        self.list.insert(0, n)

    def push_back(self, n):
        self.len += 1
        self.list.append(n)

    def pop_front(self):
        if self.len > 0:
            self.len -= 1
            return self.list.pop(0)
        else: return -1

    def pop_back(self):
        if self.len > 0:
            self.len -= 1
            return self.list.pop(-1)
        else: return -1

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def front(self):
        return  -1 if self.len == 0 else self.list[0]

    def back(self):
        return -1 if self.len == 0 else self.list[-1]

d = Deque()
for _ in range(int(input())):
    s = input().strip()
    if 'push_front' in s: d.push_front(s.split()[1])
    elif 'push_back' in s: d.push_back(s.split()[1])
    elif s == 'pop_front': print(d.pop_front())
    elif s == 'pop_back': print(d.pop_back())
    elif s == 'size': print(d.size())
    elif s == 'empty': print(d.empty())
    elif s == 'front': print(d.front())
    elif s == 'back': print(d.back())
    else: print('none')
