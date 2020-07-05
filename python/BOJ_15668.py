n = int(input())
for i in range(1, min(100000, n)):
    s = str(i) + str(n-i); l = list(); ans = 1
    for w in s:
        if w in l:
            ans = 0; break
        l.append(w)
    if ans:
        print(n - i, "+", i)
        exit(0)
print(-1)
