while True:
    n, a, w = input().split()
    a, w = map(int, [a, w])
    if n == '#': break
    elif a > 17 or w >= 80:
        print(n, 'Senior')
    else:
        print(n, 'Junior')
