N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+2)

for n in range(1, N+1):
    dp[n+1] = max(dp[n+1], dp[n])
    
    end_date = T[n-1] + n
    
    if end_date <= N+1:
        dp[end_date] = max(dp[end_date], dp[n]+P[n-1])
print(max(dp))