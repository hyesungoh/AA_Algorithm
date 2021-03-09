def solution(numbers):
    def bt(depth):
        if number: number_set.add(int(''.join(number)))
        if depth == length: return

        for i in range(length):
            if not visit[i]:
                number.append(numbers[i])
                visit[i] = True

                bt(depth+1)

                number.pop()
                visit[i] = False

    def sieve():
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(max_num ** 0.5)):
            if is_prime[i]:
                for j in range(i+i, max_num+1, i):
                    is_prime[j] = False

    length = len(numbers)
    visit = [False for _ in range(length)]
    number_set = set()
    number = []
    bt(0)

    max_num = max(number_set)
    is_prime = [True for _ in range(max_num+1)]
    sieve()

    ans = 0
    for n in number_set:
        if is_prime[n]: ans += 1

    return ans
