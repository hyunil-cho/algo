from collections import Counter

def solution(k, tangerine):
    
    counter = Counter(tangerine)
    
    sorted_keys = [ (key, value) for key, value in counter.most_common()]
    
    answer = 0
    for key_val in sorted_keys:
        if k > 0:
            k = max(0, k - (key_val[1]))
            answer+=1
    
    return answer