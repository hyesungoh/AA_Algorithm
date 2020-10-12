n = int(input())
dist = int(input())
l = [[0 for _ in range(n)] for _ in range(n)]

count = 1
y, x = n // 2, n // 2  # 시작 지점
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 방향

temp_count = 1  # 해당 방향으로 몇 번 찍어야되는지

while True:
    for i in range(4):  # 4가지 방향으로
        for j in range(temp_count):
            if count == dist:  # 목표일 때 좌표 저장
                ans = [y + 1, x + 1]

            l[y][x] = count
            y += dire[i][0]  # 현재 방향만큼 수정
            x += dire[i][1]

            if count == n * n:  # 배열의 마지막 값일 때
                [print(*t) for t in l]
                print(*ans)
                exit(1)  # 종료

            count += 1

        if i % 2 == 1:  # 같은 방향으로 진행되는 값 추가
            temp_count += 1
