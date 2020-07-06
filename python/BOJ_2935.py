n1 = input()
s = input()
n2 = input()
if s == "*":
    print('1', end='')
    print('0' * (n1.count('0') + n2.count('0')))
else:
    print(int(n1) + int(n2))

# i=input
# print(eval(i()+i()+i()))
