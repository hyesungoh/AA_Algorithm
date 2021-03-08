def solution(clothes):
    graph = {}
    for cloth in clothes:
        if cloth[1] in graph: graph[cloth[1]] += 1
        else: graph[cloth[1]] = 1


    ans = 1
    for key in graph:
        ans = ans * (graph[key] + 1)
    return ans - 1
