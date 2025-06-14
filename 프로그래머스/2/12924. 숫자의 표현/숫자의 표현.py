# 투 포인터 알고리즘
# n을 넘을 경우, 왼쪽을 이동(-)
# n을 넘지 않을 경우, 오른쪽을 이동(+)
# n일 경우, answer를 1 올리고, 왼쪽을 오른쪽 포인터로 이동할 수 있을 만큼 오른쪽으로 이동
def solution(n):
    answer = 0
    
    left = 1
    right = 1
    
    temp = 0
    
    while left <= n:
        
        if temp < n: 
            temp += right
            right += 1
        if temp == n:
            answer+=1
        if temp >= n:
            temp -= left
            left +=1
                        
    return answer