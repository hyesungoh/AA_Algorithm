def isPalin(s):
    length = len(s)
    mid = length // 2
    for i in range(mid):
        if s[i] != s[length - i - 1]:
            return "no"
    return "yes"

while True:
    s = input()
    if s == "0":
        break

    print(isPalin(s))
