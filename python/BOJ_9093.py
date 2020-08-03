for _ in range(int(input())):
    s = input().split()
    for w in s:
        print(''.join(reversed(w)), end=" ")
    print("")
