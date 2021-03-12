def solution(brown, yellow):
    total = brown + yellow
    for x in range(total, 2, -1):
        if total % x == 0:
            y = total // x
            if yellow == (x-2)*(y-2):
                return [x, y]
