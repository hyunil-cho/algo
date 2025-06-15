# 방정식 
# 길이를 X, 세로를 Y-2
# 2(X+Y-2) = brown
# (Y-2)(X-2) = yello
def solution(brown, yellow):
    
    for y in range(3, brown):
        Y = y - 2
        X = (brown // 2) -Y+2
        if (X-2) * (Y-2) == yellow:
            answer = [X,Y]
            answer.sort(reverse=True)
            return answer
    
    
    
    return []