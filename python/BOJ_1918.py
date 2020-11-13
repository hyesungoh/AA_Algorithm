s = input()
stack = []
priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}

for ch in '('+s+')':
    if ch.isupper():
        print(ch, end="")

    elif ch == "(":
        stack.append(ch)

    elif ch == ")":
        while True:
            c = stack.pop()
            if c == "(":
                break
            print(c, end="")
    else:
        while stack[-1] != "(" and priority[stack[-1]] >= priority[ch]:
            print(stack.pop(), end="")
        stack.append(ch)
