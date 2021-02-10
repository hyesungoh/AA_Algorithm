def move(num, fr, temp, to):
    if num == 1:
        print(fr, to)
    else:
        move(num-1, fr, to, temp)
        print(fr, to)
        move(num-1, temp, fr, to)

N = int(input())
print((2 ** N) - 1)
if N <= 20: move(N, 1, 2, 3)
