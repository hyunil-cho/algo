def solution(progresses, speeds):
    answer = []
    
    cur_idx = 0
    size = len(speeds)
    while cur_idx < size:
        
        for idx, next in enumerate(speeds):
            progresses[idx] += next
        
        cnt = 0
        
        while True:
            if len(progresses) > cur_idx and progresses[cur_idx] >= 100:
                cnt+=1
                cur_idx += 1
            else:
                break;
                
        if cnt > 0 :
            answer.append(cnt)
        
    
    return answer