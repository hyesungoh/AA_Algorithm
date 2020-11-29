def KMP(t, p):
    lt = len(t)
    lp = len(p)
    lps = [0 for _ in range(lp)]
    findLPS(p, lps)

    ans = 0; ans_l = [] # 일치하는 수와 일치하는 곳의 index를 저장할 변수

    i = 0 # 텍스트와 비교할 변수
    j = 0 # 패턴과 비교할 변수
    while i < lt:
        if t[i] == p[j]:
            # 문자가 같을 시 i와 j 둘 다 상승
            i += 1
            j += 1
        elif t[i] != p[j]:
            # 같지 않지만
            if j != 0:
                # 전에 문자가 같았을 시
                # lps를 이용하여 j의 값을 수정 후 재비교
                j = lps[j-1]
            else:
                # 전에 문자가 같지 않았을 시 index 이동
                i += 1

        if j == lp: # 패턴의 끝까지 동일 시
            # 정답을 위한 변수 수정
            ans += 1
            ans_l.append(i - lp + 1)
            # lps를 이용하여 j의 값을 수정 후 재비교
            j = lps[j-1]

    return ans, ans_l

def findLPS(p, lps):
    # 패턴을 이용하여 LPS( Longest proper prefix which is suffix, 접두사 이자 접미사의 최장길이 )
    # 를 찾음

    leng = 0
    i = 1
    while i < len(p):
        # 문자가 같을 시
        if p[i] == p[leng]:
            # 길이를 늘린 후 lsp 배열에 저장한 후 다음 인덱스로 넘어감
            leng += 1
            lps[i] = leng
            i += 1
        # 문자가 같지 않을 시
        else:
            if leng != 0:
                # 전에 같았으면
                # 해당 길이로 변경 후 재 비교
                leng = lps[leng-1]
            else:
                # 전에도 같지 않을 시
                # lps의 값을 0으로 저장 후 index 이동
                lps[i] = 0
                i += 1

t = input()
p = input() # 찾아야 할 패턴
ans, ans_l = KMP(t, p)
print(ans)
print(*ans_l)
