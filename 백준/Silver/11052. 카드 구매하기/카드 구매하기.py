n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dp = [0 for _ in range(n+1)]

for next in range(1, n+1):
    for sub_next in range(1, next+1):
        dp[next] = max(dp[next], dp[next-sub_next] + arr[sub_next])
print(dp[n])