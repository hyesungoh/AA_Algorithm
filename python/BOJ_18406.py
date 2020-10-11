s = input()
l = len(s)//2
print('LUCKY' if sum(map(int, s[0:l])) == sum(map(int, s[l:])) else 'READY')
