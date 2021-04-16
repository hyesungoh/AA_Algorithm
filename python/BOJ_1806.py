
INF = 100001
N, S = map(int, input().split())
L = list(map(int, input().split()))

left, right, tsum = 0, 0, 0
min_length = INF

while True:
    if tsum >= S: # 합이 구하고자하는 값보다 같거나 클 때
        min_length = min(min_length, right-left) # 최소 길이를 갱신
        tsum -= L[left]
        left += 1 # 왼쪽 값을 제외하고 탐색

    elif right == N: break # 오른쪽 끝까지 탐색시에 종료

    else: # 합이 구하고자 하는 값보다 작으며, 오른쪽 끝까지 탐색을 하지 않았을 시
        tsum += L[right]
        right += 1 # 오른쪽 값을 추가하고 범위를 넓혀 탐색

if min_length == INF: print(0) # 최대 길이와 같음 > 구하고자 하는 값보다 큰 수를 만들 수 없는 것
else: print(min_length)