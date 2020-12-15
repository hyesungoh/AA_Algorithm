MAX = 360000

def KMP(ori, pat):
    i = 0
    j = 0
    lps = getLPS(pat)
    while i < MAX*2:
        if ori[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == MAX:
            return "possible"
    return "impossible"


def getLPS(pat):
    i = 1
    leng = 0
    lps = [0 for _ in range(MAX)]
    while i < MAX:
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def checkin(p):
    l = list(map(int, input().split()))
    for i in l:
        p[i] = 1


pat = [0 for _ in range(MAX)]
ori = [0 for _ in range(MAX)]

n = int(input())
checkin(pat)
checkin(ori)
print(KMP(ori*2, pat))
