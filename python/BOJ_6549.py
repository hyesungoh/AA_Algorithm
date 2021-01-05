import sys
input = sys.stdin.readline

def checkArea(n, l):
    # 첫 연산과 마지막 사각형 확인을 위해 맨 앞과 뒤에 0 추가
    l.insert(0, 0)
    l.append(0)

    # 확인헀던 사각형의 인덱스가 들어갈 배열
    checked = [0]
    # 정담이 반환될 정수형 변수
    area = 0

    for i in range(1, n + 2):
        # l[i]는 현재 확인 중인 사각형의 높이
        # l[checked[-1]은 이전에 확인했던 최대 높이
        # checked에 값이 존재하며 현재 높이보다 이전 높이가 클 시
        while checked and (l[i] < l[checked[-1]]):
            # 비교할 사각형의 인덱스
            current_index = checked.pop()
            # i - 1 - checked[-1]은 현재 시점 사이에 몇 개의 사각형이 있는 지, 즉 가로 길이
            area = max(area, (i - 1 - checked[-1]) * l[current_index])
        checked.append(i)

    return area


while True:
    l = list(map(int, input().split()))
    n = l[0]
    if n == 0:
        break
    print(checkArea(n, l[1:]))
