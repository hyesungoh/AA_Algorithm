def solution(triangle):
    height = len(triangle)

    for y in range(1, height):
        for x in range(y+1):
            if x == 0:
                triangle[y][x] = triangle[y-1][x] + triangle[y][x]
            elif x == y:
                triangle[y][x] = triangle[y-1][x-1] + triangle[y][x]
            else:
                triangle[y][x] = max(triangle[y-1][x-1], triangle[y-1][x]) + triangle[y][x]

    return max(triangle[-1])
