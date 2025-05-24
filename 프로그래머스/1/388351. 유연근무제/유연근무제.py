# 출근 희망 시간에 늦지 않고 출근한 직원에게 상품
# 일주일동안 자신이 설정한 출근 희망 시각 + 10분까지 어플로 출근해야 합니다.
# 단, 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다
# 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 예를 들어 10시 13분은 1013이 되고 9시 58분은 958
#직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원이 몇 명인지 알고 싶습니다.
# 출근 희망 시각과 실제로 출근한 시각을 100으로 나눈 나머지는 59 이하입니다.



def solution(schedules, timelogs, startday):
    answer = 0
    
    table = {}

    for idx, next in enumerate(schedules):
        hour = next // 100
        miniute = next % 100 + 10
        
        if miniute > 59:
            miniute = miniute % 60
            hour += 1
            
        table[idx] = hour * 100 + miniute
        
        
    for idx, timelog in enumerate(timelogs):
        start_day = startday
        is_okay = True
        for next_time in timelog:
            if start_day != 6 and start_day != 7:
                if next_time > table[idx]:
                    is_okay = False
                    break
            start_day = start_day + 1 if start_day != 7 else 1
        
        if is_okay: 
            answer += 1
        
    return answer