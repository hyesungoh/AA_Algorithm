y = 0
for _ in range(int(input())):
    y = y + 1 if input() == '1' else y - 1
print('Junhee is cute!' if y > 0 else 'Junhee is not cute!')
