from fractions import Fraction

def KMP(ori, pat):
    lt = n * 2 - 1
    lp = n
    lps = getLPS(pat, n)

    ans = 0

    i = 0
    j = 0
    while i < lt:
        if ori[i] == pat[j]:
            i += 1
            j += 1
        elif ori[i] != pat[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == lp:
            ans += 1
            j = lps[j-1]

    return ans

def getLPS(pat, length):
    lps = [0 for _ in range(length)]

    j = 0
    i = 1
    while i < length:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps

n = int(input())
pat = input().replace(' ', '')
origin = input().replace(' ', '') * 2

kmp = KMP(origin[:n*2-1], pat)
frac = Fraction(kmp, n)
print("1/1" if frac == 1 else frac)
