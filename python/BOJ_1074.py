# 1074
# import sys
# sys.setrecursionlimit(100000)
# n, r, c = map(int, input().split())
# count = 0
# def z(N, x, y):
#     global count
#     if N == 2:
#         if x == r and y == c:
#             print(count)
#             return
#         count += 1
#
#         if x + 1 == r and y == c:
#             print(count)
#             return
#         count += 1
#
#         if x == r and y + 1 == c:
#             print(count)
#             return
#         count += 1
#
#         if x + 1 == r and y + 1 == c:
#             print(count)
#             return
#         count += 1
#
#     else:
#         z(N//2, y, x)
#         z(N//2, y, x+N//2)
#         z(N//2, y+N//2, x)
#         z(N//2, y+N//2, x+N//2)
# z(n*n, 0, 0)

n, r, c = map(int, input().split())
count = 0
while n > 0:
    if n == 1: # 목표 좌표가 2사분면일 때
        if r == 0 and c == 1: # 오른쪽 위
            count += 1
        elif r == 1 and c == 0: # 아래
            count += 2
        elif r == 1 and c == 1: # 오른쪽 아래
            count += 3
    else: # 목표 좌표가 사
        temp = (2 ** n) // 2  # 현재 n의 배열 크기 ex) 2 == 4, 3 == 8
        if temp > r and temp <= c: # 목표 좌표가 1사분면에 있을 때
            count += temp ** 2 # 2사분면의 크기만큼 더함
            c -= temp # 다음 반복에서 계산을 위해
        elif temp <= r and temp > c: # 목표 좌표가 3사분면에 있을 때
            count += (temp ** 2) * 2 # 1, 2사분면의 크기만큼 더함
            r -= temp # 다음 반복에서 계산을 위해
        elif temp <= r and temp <= c: # 목표 좌표가 4분면에 있을 때
            count += (temp ** 2) * 3 # 1, 2, 3사분면의 크기만큼 더함
            r -= temp # 다음 반복에서 계산을 위해
            c -= temp
    n -= 1 # 현재 배열을 4등분 n = 3, temp = 8 > n = 2, temp = 4
print(count)
