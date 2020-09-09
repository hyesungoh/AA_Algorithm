# pokemon_list = []
# n, m = map(int, input().split())
# for _ in range(n):
#     pokemon_list.append(input())
#
# for _ in range(m):
#     s = input()
#     try:
#         s = int(s)
#         print(pokemon_list[s-1])
#     except:
#         print(pokemon_list.index(s)+1)

import sys
input = sys.stdin.readline

pokemon_list = []
pokemon_dict = {}

n, m = map(int, input().split())
for i in range(n):
    s = input().rstrip()
    pokemon_list.append(s)
    pokemon_dict[s] = i+1

for _ in range(m):
    s = input().rstrip()
    try:
        s = int(s)
        print(pokemon_list[s-1])
    except:
        print(pokemon_dict[s])

# import sys
# input = sys.stdin.readline
#
# pokemon_list = []
# pokemon_dict = {}
#
# n, m = map(int, input().split())
# for i in range(n):
#     s = input().rstrip()
#     pokemon_list.append(s)
#     pokemon_dict[s] = i+1
#
# for _ in range(m):
#     s = input().rstrip()
#     if s.isdigit():
#         print(pokemon_list[int(s)-1])
#     else:
#         print(pokemon_dict[s])
