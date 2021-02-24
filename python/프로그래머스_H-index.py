def solution(cita):
    length = len(cita)
    cita.sort(reverse=True)

    for i in range(length):
        if i >= cita[i]:
            return i

    return length
