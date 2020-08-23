a, b, c = map(int, input().split())
count_a = [a, b, c].count(a)
count_b = [a, b, c].count(b)

if count_a == 1 and count_b == 1:
    n = 0
    num = max(a, b, c)
elif count_a >= count_b:
    n = count_a
    num = a
else:
    n = count_b
    num = b


if n == 3:
    print(10000 + num * 1000)
elif n == 2:
    print(1000 + num * 100)
else:
    print(num * 100)


# a, b, c = sorted(map(int, input().split()))
# if a == c:
#     print(10000 + a * 1000)
# elif a == b or b == c:
#     print(1000 + b * 100)
# else:
#     print(c * 100)
