def solution(numbers):
    answers = set()
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            answers.add(numbers[i] + numbers[j])

    return list(sorted(answers))
