import sys
sys.setrecursionlimit(10**6)

def check(word):
    vowel_cnt = 0
    cont_cnt = 0

    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u']: vowel_cnt += 1
        else: cont_cnt += 1

        if vowel_cnt >= 1 and cont_cnt >= 2: return True
    return False


def bt(depth, temp_word):
    if depth == l:
        if check(temp_word):
            print("".join(temp_word))
        return

    for i in range(c):
        if not visit[i] and (not temp_word or temp_word[-1] < words[i]):
            visit[i] = True
            temp_word.append(words[i])
            bt(depth+1, temp_word)

            visit[i] = False
            temp_word.pop()

l, c = map(int, input().split())
words = sorted(input().split())
visit = [False for _ in range(c)]
bt(0, [])
