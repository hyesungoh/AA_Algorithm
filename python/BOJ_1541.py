s = input()
ans = []
for i in s.split('-'):
    ans.append(str(eval("+".join(list(map(str, map(int, i.split('+'))))))))

d = "-".join(ans)
print(eval(d))
