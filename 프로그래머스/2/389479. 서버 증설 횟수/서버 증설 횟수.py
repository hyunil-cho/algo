def solution(players, m, k):
    answer = 0
    servers = [0 for _ in range(0,24)]
    cur_cnt = 0
    
    for idx, player in enumerate(players):
        removed_idx = idx - k
        if removed_idx >= 0:
            cur_cnt-=servers[removed_idx]
            servers[removed_idx] = 0
        need_num = cur_cnt - getNums(m, player)    
        if need_num < 0:
            servers[idx] += need_num * -1
            cur_cnt += need_num * -1
            answer+=need_num * -1

    return answer

def getNums(m, cnt):
    return int(cnt / m)
    