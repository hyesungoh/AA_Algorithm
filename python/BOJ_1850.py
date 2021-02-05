# a, b = map(lambda x: int("1" * int(x)), input().split())
a, b = map(int, input().split())
while b != 0: a, b = b, a % b
print("1" * a)
