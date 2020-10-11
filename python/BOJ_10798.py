# l = []
# for _ in range(5):
#     l.append(input())
# for i in range(15):
#     for j in range(5):
#         try:
#             print(l[j][i], end='')
#         except:
#             continue

# l = [input() for _ in range(5)]
# for i in range(15):
#     for j in range(5):
#         try: print(l[j][i], end='')
#         except: continue

l = [input() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if len(l[j]) > i:
            print(l[j][i], end='')
