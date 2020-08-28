Y, M = 0, 0
input()
for i in map(int, input().split()):
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15
print('M ' + str(M) if Y > M else 'Y M ' + str(M) if Y == M else 'Y ' + str(Y))
