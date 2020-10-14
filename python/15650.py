n, m = map(int, input().split())
l = list(range(1, n+1))
visit = [False] * n
ans = []

# def bt(index):
#     if index == m:
#         print(*ans)
#         return
#
#     for i in range(n):
#         if visit[i]:
#             continue
#
#         ans.append(l[i])
#         visit[i] = True
#         bt(index+1)
#         ans.pop()
#
#         for j in range(i+1, n):
#             visit[j] = False
# bt(0)

def bt(depth, index):
    if depth == m: # 크기와 같을 떄 출력하고 함수 종료
        print(*ans)
        return

    for i in range(index, n): # 이미 들어간 값이 있다면 해당 값보다 큰 것만 반복
        if not visit[i]: # 방문하지 않았던 것일 때
            ans.append(l[i])
            visit[i] = True
            bt(depth+1, i+1) # 현재 반복중인 i를 index로
            visit[i] = False
            ans.pop() # 재귀적으로 호출할 때를 위해 맨 뒤에 append한 값을 삭제
bt(0, 0)
