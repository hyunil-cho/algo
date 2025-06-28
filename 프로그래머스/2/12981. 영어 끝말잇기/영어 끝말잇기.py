def solution(n, words):
    answer = []
    dic = set()
    
    last_val = words[0]
    dic.add(last_val)
    cur_player = 1
    cur_idx = 1
    cur_cnt = 1
    words_len = len(words)
    
    while True:
        next_val = words[cur_idx]
        if last_val[-1] != next_val[0]:
            print(last_val, next_val)
            return [(cur_player % n) +1 , cur_cnt]
        if next_val in dic:
            return [(cur_player % n) +1 , cur_cnt]
        
        cur_idx += 1
        cur_player = (cur_player+1) % n
        last_val = next_val
        dic.add(next_val)
        
        if cur_player == 0:
            cur_cnt += 1
        
        if cur_idx == words_len:
            break;
        

    return [0,0]