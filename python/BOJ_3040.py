l, s, d = [], 0, False
for _ in range(9):
    n = int(input())
    l.append(n); s += n

for i in range(9):
    for j in range(i+1, 9):
        t1, t2 = l[i], l[j]
        if t1 + t2 == s - 100:
            l.remove(t1)
            l.remove(t2)
            d = True
            break
    if d: break

[print(i) for i in sorted(l)]

# a=[]
# for i in range(9):a.append(int(input()))
# b=sum(a)
# for i in a:
#     c=b-100-i
#     if c in a and i!=c:a.remove(i);a.remove(c)
# for i in a:print(i)
