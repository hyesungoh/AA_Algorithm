n = int(input())
stage, key = 1, 1
while stage + key <= n:
    key += stage
    stage += 1
step = n - key
x, y = step + 1, stage - step
if stage % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))
