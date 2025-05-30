import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n+1)]

for idx in range(1, n+1):
    dp[idx] = max(dp[idx], dp[idx-1])
    end_date = idx + t[idx] -1
    if end_date <= n:
        dp[end_date] = max(dp[end_date], dp[idx-1]+p[idx])
print(dp[n])