# 첫 풀이
n = int(input())
for i in range(n*2):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

# 다른 풀이
n = int(input())
for i in range(n):
    print("* " * (n - n//2))
    print(" *" * (n//2))
