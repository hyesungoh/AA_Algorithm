def solution(s):
    answer = False
    balance = 0

    for t in s:
        if t == ")" and balance == 0:
            return False
        balance += -1 if t == ")" else 1
        answer = balance == 0

    return answer
