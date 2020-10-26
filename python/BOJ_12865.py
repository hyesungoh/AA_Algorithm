import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w_v = [[0, 0]]
ans = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    w_v.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = w_v[i][0] # 무게
        v = w_v[i][1] # 가치
        if j < w: # 들 수 없으면 ?
            ans[i][j] = ans[i-1][j] # 같은 무게, 저번 반복된 물건의 값
        else: # 들 수 있다면?
            # 같은 무게, 저번 반복된 물건의 값과
            # 현재 물건의 가치 + 저번 반복된 물건의 현재 반복된 무게 - 현재 물건의 무게의 값을 더한 값을
            # 비교해서 더욱 큰 것을 배열에 할당
            ans[i][j] = max(ans[i-1][j], v + ans[i-1][j-w])
print(ans[n][k])
