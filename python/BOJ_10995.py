# n = int(input())
# for i in range(n):
#     print('* '*n if i % 2 == 0 else " *"*n)

n=int(input())
[print('* '*n if i%2==0 else " *"*n) for i in range(n)]
