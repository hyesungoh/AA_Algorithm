l = [1,2,4]

for _ in range(7):
    l.append(sum(l[-3::]))

for _ in range(int(input())):
    print(l[int(input())-1])
