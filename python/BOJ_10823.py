import sys
l = sys.stdin.readlines()
s = ""
for i in l:
    s += i.replace('\n', '')
print(sum(map(int, s.split(','))))
