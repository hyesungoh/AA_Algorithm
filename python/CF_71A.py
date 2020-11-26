for _ in range(int(input())):
    s = input()
    l = len(s)
    if l > 10:
        print(s[0]+str(l-2)+s[-1])
    else:
        print(s)
