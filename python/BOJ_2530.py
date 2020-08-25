h, m, s = map(int, input().split())
total = (h*60*60) + (m*60) + s + int(input())
total %= (24*60*60)
print(total // 3600, (total % 3600) // 60, (total % 3600) % 60)
