def getLPS(t, lps):
    leng = 0
    i = 1

    while i < len(t):
        if t[i] == t[leng]:
            leng += 1
            lps[i] = leng
            i += 1

        else:
            if leng != 0:
                leng = lps[leng-1]

            else:
                lps[i] = 0
                i += 1
n = int(input())
t = input()
lps = [0 for _ in range(n)]
getLPS(t, lps)
ans = n - lps[n-1]
print(ans)
