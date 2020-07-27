# a,b,v = map(int, input().split())
# t = 0
# while 1:
#     t += 1
#     if v <= (a-b)*t + a:
#         break
#
# print(t+1)
a,b,v = map(int, input().split())
t = ((v-b) // (a-b))
print(t if (v-b) % (a-b) == 0 else t+1)
# 4 1 5 = 2
# 5-1 % 4-1 = 1
# 5-1 // 4-1 = 1

# 2 1 5 = 4
# 5-1 % 2-1 = 0
# 5-1 // 2-1 = 4

a,b,v=map(int,input().split())
print((v-b-1)//(a-b)+1)
# 4 1 5 = 2
# (5 - 1 - 1) // (4 - 1) + 1 = 2

# 2 1 5 = 4
# (5 - 1 - 1) // (2 - 1) + 1 = 4
