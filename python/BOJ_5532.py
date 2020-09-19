l = []
for _ in range(5):
    l.append(int(input()))
n1 = (l[1] // l[3] + 1 if l[1] / l[3] > l[1] // l[3] else l[1] // l[3])
n2 = (l[2] // l[4] + 1 if l[2] / l[4] > l[2] // l[4] else l[2] // l[4])
print(l[0] - max(n1, n2))

# n,a,b,q,w=map(lambda x: int(input()),range(5))
# print(n-max((a+q-1)//q,(w+b-1)//w))
