n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

dp[1] = [1 for _ in range(10)]

for row in range(2, n+1):
  for col in range(0, 10):
    for z in range(col, 10):
        dp[row][col] += dp[row-1][z]
        dp[row][col] %= 10007
print(sum(dp[n]) % 10007)
    