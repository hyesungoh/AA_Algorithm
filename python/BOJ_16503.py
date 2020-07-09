# s = input().split()
# s = ['//' if i == '/' else i for i in s]
# s.insert(0, '('); s.insert(4, ')')
# x = eval(''.join(s))
# s.remove('('); s.remove(')')
# s.insert(2, '('); s.insert(6, ')')
# y = eval(''.join(s))
#
# print(min(x, y))
# print(max(x, y))

s = ['//' if i == '/' else i for i in input().split()]

x = eval(''.join(s[0:3]))
if s[3] == '//' and x < 0:
    x = -(eval(str(abs(x)) + ''.join(s[3:5])))
else:
    x = eval(str(x) + ''.join(s[3:5]))

y = eval(''.join(s[2:5]))
if s[1] == '//' and y < 0:
    y = -(eval(''.join(s[0:2]) + str(abs(y))))
else:
    y = eval(''.join(s[0:2]) + str(y))

print(min(x, y))
print(max(x, y))

# a,b,c,d,e=input().split()
# f=int(eval(str(int(eval(a+b+c)))+d+e))
# s=int(eval(a+b+str(int(eval(c+d+e)))))
# print(min(f,s))
# print(max(f,s))
