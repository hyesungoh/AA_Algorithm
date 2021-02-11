def move(n, x, y, z):
    if n == 1:
        print(x, z)
    else:
        move(n-1, x, z, y)
        print(x, z)
        move(n-1, y, x, z)

n = int(input())
print((2 ** n) - 1)
move(n, 1, 2, 3)
