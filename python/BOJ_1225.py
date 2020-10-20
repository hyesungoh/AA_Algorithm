n, m = input().split(); ans = 0
n = n.replace('0', '')
m = m.replace('0', '')
for i in n:
    for j in m:
        ans += int(i)*int(j)
print(ans)
