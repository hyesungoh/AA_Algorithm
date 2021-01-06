import sys
input = sys.stdin.readline

def checkArea(n, l):
    checked = [0]
    area = 0

    for i in range(1, n+2):
        while checked and (l[i] < l[checked[-1]]):
            current_height = checked.pop()
            area = max(area, (i - 1 - checked[-1]) * l[current_height])
        checked.append(i)

    return area

n = int(input())
l = [0]
for _ in range(n):
    l.append(int(input()))
l.append(0)
print(checkArea(n, l))
