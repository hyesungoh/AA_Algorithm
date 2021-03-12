def lower_bound(start, end, num):
    while start < end:
        mid = (start + end) // 2
        if dp[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end

n = int(input())
l = list(map(int, input().split()))
dp = []

for num in l:
    if len(dp) == 0:
        dp.append(num)
        continue

    if dp[-1] < num:
        dp.append(num)
    else:
        idx = lower_bound(0, len(dp)-1, num)
        dp[idx] = num

print(len(dp))
