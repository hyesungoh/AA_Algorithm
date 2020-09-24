l = [0, 1, 2]
for _ in range(9997):
    l.append(sum(l[-2::]))
print(l[int(input())] % 10007)
