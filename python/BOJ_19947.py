# 19947
def investment(money, year):
    global ans
    if year == 0:
        ans = max(ans, money)
        return

    if year - 1 >= 0:
        interest = int(money * 1.05)
        investment(interest, year - 1)
    if year - 3 >= 0:
        interest = int(money * 1.2)
        investment(interest, year - 3)
    if year - 5 >= 0:
        interest = int(money * 1.35)
        investment(interest, year - 5)

h, y = map(int, input().split())
ans = 0
investment(h, y)
print(ans)


# def invest(money, year):
#     ans = money
#     if year >= 1:
#         ans = max(ans, invest(int(money * 1.05), year-1))
#     if year >= 3:
#         ans = max(ans, invest(int(money * 1.2), year-3))
#     if year >= 5:
#         ans = max(ans, invest(int(money * 1.35), year-5))
#     return ans
#
# h, y = map(int, input().split())
# print(invest(h, y))


# def e(h, y):
#     m=h
#     if y>=1: m=max(m,e(int(h*1.05),y-1))
#     if y>=3: m=max(m,e(int(h*1.2),y-3))
#     if y>=5: m=max(m,e(int(h*1.35),y-5))
#     return m
# h, y = map(int, input().split())
# print(e(h,y))
