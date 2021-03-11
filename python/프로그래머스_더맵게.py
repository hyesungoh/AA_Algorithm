import heapq

def solution(scov, k):
    heapq.heapify(scov)
    cnt = 0
    length = len(scov)
    first = heapq.heappop(scov)

    while length > 1:
        second = heapq.heappop(scov)
        first = heapq.heappushpop(scov, first + second + second)

        if first >= k:
            return cnt + 1
        cnt += 1
        length -= 1

    return -1
