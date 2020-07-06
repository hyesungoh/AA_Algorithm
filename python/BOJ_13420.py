for _ in range(int(input())):
    s, a = input().split('=')
    print("correct") if eval(s) == int(a) else print("wrong answer")
