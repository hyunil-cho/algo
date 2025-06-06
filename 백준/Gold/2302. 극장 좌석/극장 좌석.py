def count_arrangements(n, vip_list):
    # 피보나치 배열 초기화 (최대 좌석 수는 40이므로 충분히 크게)
    dp = [0] * 41
    dp[0] = 1  # 좌석 0개인 경우: 1가지 방법 (아무것도 안함)
    dp[1] = 1  # 좌석 1개: 1가지 방법
    for i in range(2, 41):
        dp[i] = dp[i - 1] + dp[i - 2]

    result = 1
    prev_vip = 0  # 맨 앞부터 시작
    
    for vip in vip_list:
        segment_len = vip - prev_vip-1
        result *= dp[segment_len]
        prev_vip = vip
   
    result *= dp[n- prev_vip]

    return result


# 📥 입력 처리
n = int(input())  # 좌석 수
m = int(input())  # VIP 수
vip_list = [int(input()) for _ in range(m)]

# ✅ 결과 출력
print(count_arrangements(n, vip_list))
