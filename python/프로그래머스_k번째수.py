def solution(array, commands):
    answer = []

    for s, e, k in commands:
        tarr = sorted(array[s - 1:e])
        answer.append(tarr[k - 1])

    return answer
