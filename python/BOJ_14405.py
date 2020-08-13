s = input()
s = s.replace('pi', '/')
s = s.replace('ka', '/')
s = s.replace('chu', '/')
print('YES' if s in '/'*5000 else 'NO')

# print('NO' if input().replace('pi', ' ').replace('ka', ' ').replace('chu', ' ').strip() else 'YES')
