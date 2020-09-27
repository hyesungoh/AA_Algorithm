import bisect
import sys
from collections import deque
input = sys.stdin.readline

class Dpq:
    def __init__(self):
        self.q = deque()
        self.d = dict()

    def input(self, n):
        try:
            self.d[n] += 1
        except:
            self.d[n] = 1
            bisect.insort_left(self.q, n) # 이진탐색을 이용해 위치파악 후 삼입

    def remove(self, n):
        if not self.q:
            pass
        elif n == 1:
            if self.d[self.q[-1]] == 1:
                self.d.pop(self.q[-1])
                self.q.pop()
            else:
                self.d[self.q[-1]] -= 1
        else:
            if self.d[self.q[0]] == 1:
                self.d.pop(self.q[0])
                self.q.popleft()
            else:
                self.d[self.q[0]] -= 1

    def print(self):
        if not self.q:
            print('EMPTY')
        else:
            print(self.q[-1], self.q[0])

for _ in range(int(input())):
    dpq = Dpq()
    for _ in range(int(input())):
        s, n = input().split()
        n = int(n)
        if s == "I":
            dpq.input(n)
        else:
            dpq.remove(n)
    dpq.print()
