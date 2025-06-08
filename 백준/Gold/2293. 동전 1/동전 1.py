def sol(k, values):
  values = [0] + values
  dp = [0 for _ in range(k+1)]

  dp[0] = 1

  for idx in range(1,len(values)):
    val = values[idx]
    for next in range(1, k+1):
      if next - val >= 0:
          dp[next] += dp[next-val]

  print(dp[k])


n,k = map(int,input().split())
arr = [int(input()) for y in range(n)]
sol(k, arr)
