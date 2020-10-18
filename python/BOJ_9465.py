import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()); l = []
    l.append(list(map(int, input().split())))
    l.append(list(map(int, input().split())))
    l[0][1] += l[1][0] # 두번째 값에 왼쪽 대각선 값을 더함
    l[1][1] += l[0][0]
    for i in range(2, n): # 두번째부터 배열의 n번째까지
        l[0][i] += max(l[1][i-1], l[1][i-2]) # 왼쪽 대각선값과 그 왼쪽의 값의 크기를 비교해서 큰 것을 더
        l[1][i] += max(l[0][i-1], l[0][i-2])
    print(max(l[0][n-1], l[1][n-1])) # 배열의 마지막 값 중 큰 것을 출력
