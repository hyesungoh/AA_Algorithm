from collections import deque

def solution(pri, loca):
    docs = deque([i for i in range(len(pri))])
    pri = deque(pri)
    ans = 1

    while docs:
        n_doc = docs.popleft()
        n_pri = pri.popleft()

        for o_pri in pri:
            if o_pri > n_pri:
                pri.append(n_pri)
                docs.append(n_doc)
                break
        else:
            if n_doc == loca:
                return ans
            ans += 1
