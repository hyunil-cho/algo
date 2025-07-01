def solution(n,a,b):
    answer = 1
    a = a-1
    b = b-1
    
    while (a // 2) != ( b // 2):
        a = a//2;
        b = b//2;
        answer += 1
        
    
    
        
    return answer