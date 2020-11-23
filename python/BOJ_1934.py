def uc(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return (x * y //uc(x, y))

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(lcm(n, m))
