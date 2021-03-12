def solution(n, times):
    answer = 0

    length = len(times)
    start, end = 1, (length+1) * max(times)
    while start <= end:
        mid = (start + end) // 2

        count = 0
        for time in times:
            count += mid // time
            if count >= n: break

        if count >= n:
            answer = mid
            end = mid - 1
        else: start = mid + 1

    return answer
