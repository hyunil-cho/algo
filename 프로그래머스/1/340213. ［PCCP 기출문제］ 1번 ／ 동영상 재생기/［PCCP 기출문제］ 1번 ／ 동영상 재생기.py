# 10초 전으로 이동 시, 0초를 초과할 경우, 0
# 10초 후로 이동 시, 길이를 초과할 경우 최대 길이

def time_to_mmss(time):
    mm = str(time // 60)
    mm = "0"+mm if len(mm) < 2 else mm;
    ss = str(time % 60)
    ss = "0"+ss if len(ss) < 2 else ss;
    return mm+":"+ss

def mmss_to_time(mmss):
    mm, ss = mmss.split(":")
    return int(mm) * 60 + int(ss);
    
def solution(video_len, pos, op_start, op_end, commands):
    
    cur_time = mmss_to_time(pos)
    max_time = mmss_to_time(video_len)
    op_start = mmss_to_time(op_start)
    op_end = mmss_to_time(op_end)
    
    cur_time = cur_time if cur_time <op_start or cur_time > op_end else op_end
    
    for command in commands:
        if command=='next':
            cur_time = min(cur_time+10, max_time)
        elif command =='prev' :
            cur_time = max(0, cur_time-10)
        if cur_time >= op_start and cur_time <= op_end:
            cur_time = op_end
            
    return time_to_mmss(cur_time)

