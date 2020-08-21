s = 0
for _ in range(int(input())):
    s += int(input())
if s == 0: print(0)
else:
    print('+' if s > 0 else '-')
