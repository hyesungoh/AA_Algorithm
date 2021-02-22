def solution(n):
    s = "124"
    dp = [s[(n-1) % 3]]

    while n > 3:
        n = (n-1) // 3
        dp.append(s[(n-1)%3])

    return "".join(reversed(dp))
