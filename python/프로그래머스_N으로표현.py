def solution(N, number):
    if N == number:
        return 1

    sets = []
    for i in range(1, 8):
        t = [int(str(N) * i)]
        sets.append(set(t))

    for i in range(1, 8):
        for j in range(i):
            for i_set in sets[j]:
                for j_set in sets[i-j-1]:
                    sets[i].add(i_set + j_set)
                    sets[i].add(i_set - j_set)
                    sets[i].add(i_set * j_set)
                    if j_set != 0:
                        sets[i].add(i_set // j_set)

        if number in sets[i]:
            return i + 1
    else:
        return -1
