import re

def solution(dartResult):
    
    pattern = r"(10|[0-9])([SDT])([*#]?)"    
    result = re.findall(pattern, dartResult)
    
    scores = [0,0,0]
    
    for idx, val in enumerate(result):
        print(idx, val)
        scores[idx] = int(val[0])
        ample = val[1]
        
        if ample =='S':
            scores[idx] **= 1
        elif ample =='D':
            scores[idx] **= 2
        else:
            scores[idx] **= 3
            
        bonus = val[2]
        
        if len(bonus) == 0 :
             continue
        
        if bonus =='*':
            scores[idx] *= 2
            if idx > 0:
                scores[idx-1] *= 2
        else:
            scores[idx] *= -1
     
    
    return sum(scores)