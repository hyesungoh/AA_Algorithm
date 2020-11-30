import sys
input = sys.stdin.readline

def getLPS(s, ls):
    lps = [0 for _ in range(ls)]

    leng = 0
    i = 1
    while i < ls:
        if s[i] == s[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

while True:
    s = input().rstrip()
    if s == ".":
        break
    ls = len(s)
    lps = getLPS(s, ls)
    pat_len = ls - lps[-1]
    print(ls // pat_len if ls % pat_len == 0 else 1)
