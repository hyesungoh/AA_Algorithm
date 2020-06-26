temp, j = 0, 0
for i in range(1,10):
    x = int(input())
    if  x > temp:
        j = i
        temp = x
print(temp)
print(j)

# x=[int(input()) for a in range(9)]
# print(max(x),x.index(max(x))+1)
