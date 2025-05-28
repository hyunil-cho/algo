N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 2)  # N+1일에 퇴사, 인덱스는 N+1까지 필요

for i in range(1, N + 1):
    # 1-based로 index 조정
    # 상담을 하지 않는 경우
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담을 하는 경우
    if i + T[i - 1] <= N + 1:
        dp[i + T[i - 1]] = max(dp[i + T[i - 1]], dp[i] + P[i - 1])

print(max(dp))