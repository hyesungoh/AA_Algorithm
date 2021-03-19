# n = int(input())
# cranes = sorted(map(int, input().split()))
# min_crane = min(cranes)
# m = int(input())
# boxes = sorted(map(int, input().split()))
#
# cnt, answer = 0, 0
#
# while True:
#     if cnt >= m: break
#
#     length = cnt+n if cnt+n < m else m if cnt == m-1 else -1
#     now_boxes = boxes[cnt:length]
#     max_box = now_boxes[-1]
#
#     if min_crane >= max_box:
#         cnt += n
#
#     else:
#         for crane in cranes:
#             # print(crane, boxes[cnt])
#             if cnt >= m: break
#
#             if crane >= boxes[cnt]:
#                 cnt += 1
#                 continue
#             if crane == cranes[-1] and crane < boxes[cnt]:
#                 print(-1)
#                 exit(0)
#
#     answer += 1
#
# print(answer)

n = int(input())
cranes = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

answer = 0
while m > 0:
    answer += 1
    for crane in cranes:
        for i in range(m):
            if crane >= boxes[i]:
                del boxes[i]
                m -= 1
                break

print(answer)
