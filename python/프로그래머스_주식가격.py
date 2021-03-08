from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []

    while prices:
        now = prices.popleft()
        cnt = 0
        for next in prices:
            cnt += 1
            if now > next: break
        answer.append(cnt)

    return answer
