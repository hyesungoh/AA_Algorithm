import sys
input = sys.stdin.readline

braket_fair = {")": "(", "]": "["}

while True:
    stack = []
    answer = True
    string = input().rstrip()

    if string == ".": break

    for word in string:
        if word == "(" or word == "[": stack.append(word)
        elif word == ")" or word == "]":
            if stack and stack[-1] == braket_fair[word]:
                stack.pop()
            else:
                answer = False
                break

    if len(stack) != 0: answer = False
    print("yes" if answer else "no")
