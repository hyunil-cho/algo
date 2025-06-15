# 가장 쉬운 방법은, 1을 더하는 것 -> 가장 아래 위치한 비트가 0일 경우
# 가장 뒤에서 두 번째 비트가 0일 경우, 마지막이 1 이어도 1을 더하는 것이 유리함
# 
def solution(n):
    target_bin = bin(n)[2:].count("1")
    next = n+1
    while True:
        next_bin = bin(next)[2:].count("1")
        if target_bin == next_bin:
            return next
        next += 1
    return next