def solution(n):
    answer = 0
    
    for next in range(0, n+1, 2):
        answer += next
    
    return answer