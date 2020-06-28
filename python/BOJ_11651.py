l = list()
for _ in range(int(input())):
    l.append(list(map(int, input().split())))

l.sort(key= lambda x: (x[1], x[0]))
[print(i[0], i[1]) for i in l]
