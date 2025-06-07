def solution(n, first_row, second_row):
    dp = [[0,0] for _ in range(n)]
    dp[0][0] = first_row[0]
    dp[0][1] = second_row[0]

    for next in range(1, n):
        dp[next][0] = max(dp[next-1][0], dp[next-1][1]+first_row[next])
        dp[next][1] = max(dp[next-1][1], dp[next-1][0]+second_row[next])

    print(max(dp[n-1]))

num = int(input())

for _ in range(num):
    n = int(input())
    first_row = list(map(int, input().split()))
    second_row = list(map(int, input().split()))
    solution(n, first_row, second_row)