def solution(msg):
    answer = []
    _dict = init()
        
    cur_idx = 0
    last_idx = len(msg)
    
    
    while cur_idx < last_idx:
        offset = 0
        while cur_idx + offset <= last_idx:
            cur_msg = msg[cur_idx: cur_idx + offset+1]
            if cur_msg in _dict:
                offset+=1
            else:
                _dict[cur_msg] = len(_dict)+1
                break;
        item = msg[cur_idx : cur_idx+offset]
        answer.append(_dict[item])
        cur_idx += offset
        
        
    return answer

def init():
    _dict = {}
    idx = 1
    for i in range(ord('A'), ord('Z') + 1):
        _dict[chr(i)] = idx
        idx+=1
    return _dict
