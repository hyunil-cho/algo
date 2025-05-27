from collections import Counter

def solution(participant, completion):
    
    counter = dict(Counter(participant))
    
    for n in completion:
        cur_cnt = counter[n]-1
        
        if cur_cnt == 0:
            del counter[n]
        else:
            counter[n] = cur_cnt
    
    
    return list(counter.keys())[0]