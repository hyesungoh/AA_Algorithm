# b, n = 2000, 2000
# b = min(b, int(input()))
# b = min(b, int(input()))
# b = min(b, int(input()))
# n = min(n, int(input()))
# n = min(n, int(input()))
# print(b+n-50)

i = lambda:int(input())
b = min(i(), i(), i())
n = min(i(), i())
print(b+n-50)
