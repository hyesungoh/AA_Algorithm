n, m = map(int, input().split())
l = list(range(1, n+1))
visit = [False] * n
ans = []

# def bt(index):
#     if index == m: # 크기가 같을 떄
#         print(*ans)
#         return
#
#     for i in range(n): # 입력받은 수-1 까지 반복
#         if visit[i]: # 이미 사용한 수일 때 넘어감
#             continue
#
#         ans.append(l[i]) # 배열에 해당 값 추가
#         visit[i] = True # 방문 확인 배열에 값 수정
#         bt(index+1) # 크기를 늘려 재귀적 호출
#         ans.pop() # 다음 반복을 위해 배열의 마지막 값 제거
#
#         for j in range(i+1, n): # 현재 수보다 큰 수들을 전부 미방문 처리
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
