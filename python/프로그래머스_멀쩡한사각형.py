def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    n = gcd(w, h)
    return (w * h) - (w + h - n)

# from math import gcd
#
# def solution(w, h):
#     return (w * h) - (w + h - gcd(w, h))
