l = [1, 1, 1, 2, 2]
for i in range(5, 100):
    l.append(l[i-5] + l[i-1])
for _ in range(int(input())):
    print(l[int(input())-1])
