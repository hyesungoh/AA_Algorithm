l = list()
for _ in range(int(input())):
    l.append(list(map(int, input().split())))

l.sort(key= lambda x: (x[0], x[1]))
[print(i[0], i[1]) for i in l]
