# import heapq
#
# def solution(tickets):
#     graph = {i[0]: [] for i in tickets}
#
#     for ticket in tickets:
#         fr = ticket[0]
#         to = ticket[1]
#         heapq.heappush(graph[fr], to)
#
#     q = ['ICN']
#     answer = []
#     while q:
#         now = q.pop()
#         answer.append(now)
#         if now in graph and graph[now]:
#             next = heapq.heappop(graph[now])
#             q.append(next)
#
#     return answer

def solution(tickets):
    graph = {i[0]: [] for i in tickets}

    for ticket in tickets: graph[ticket[0]].append(ticket[1])
    for k in graph: graph[k].sort(reverse=True)

    stack = ['ICN']
    answer = []
    while stack:
        top = stack[-1]
        if top in graph and graph[top]: stack.append(graph[top].pop())
        else: answer.append(stack.pop())

    return answer[::-1]
