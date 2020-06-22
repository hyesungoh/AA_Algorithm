h, m = list(map(int, input().split()))
m -= 45
if m < 0:
    if h == 0:
        print(23, 60 + m)
    else:
        print(h-1, 60 + m)
else:
    print(h, m)
