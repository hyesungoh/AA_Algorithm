from bisect import bisect_left

n = int(input())
l = list(map(int, input().split()))
dp = [0 for _ in range(n)]
cmp = [] # 이분탐색을 위해
maxVal = 0 # 최대값

for i in range(n):
    if i == 0: # 첫 번째일 때 추가만
        cmp.append(l[i])
        continue

    if cmp[-1] < l[i]: # 저장된 값과 비교하여 클 시
        cmp.append(l[i])
        dp[i] = len(cmp) -1
        maxVal = dp[i]
    else:
        # 작을 시 어느 위치의 값에 해당하는 지
        dp[i] = bisect_left(cmp, l[i])
        cmp[dp[i]] = l[i]

# 최대 길이 출력
print(maxVal + 1)

# 인덱스별 길이를 기준으로 수열 저장
res = []
for i in range(n-1, -1, -1):
    if dp[i] == maxVal:
        res.append(l[i])
        maxVal -= 1
res.reverse()

print(*res)
