

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    length = len(truck_weights)
    exit_length = 0

    bridge_now = deque([0 for _ in range(bridge_length)])
    bridge_weight = 0
    answer = 0

    while exit_length != length:
        if truck_weights:
            truck_now = truck_weights.popleft()
        last_truck = bridge_now[-1]

        if bridge_weight + truck_now - last_truck <= weight:
            bridge_now.appendleft(truck_now)
            bridge_weight += truck_now
        else:
            bridge_now.appendleft(0)
            truck_weights.appendleft(truck_now)

        bridge_now.pop()
        bridge_weight -= last_truck
        exit_length += 1 if last_truck != 0 else 0
        answer += 1

    return answer


# def solution(bride_length, weight, truck_weights):
#     answer = 0
#     truck_weights = deque(truck_weights)
#     bridge_now = deque([0 for _ in range(bride_length)])
#     bridge_total = 0
#
#     while bridge_now:
#         answer += 1
#         bridge_total -= bridge_now.popleft()
#
#         if truck_weights:
#             if bridge_total + truck_weights[0] <= weight:
#                 t = truck_weights.popleft()
#                 bridge_now.append(t)
#                 bridge_total += t
#             else:
#                 bridge_now.append(0)
#
#     return answer
