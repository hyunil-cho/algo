# t초 동안 붕대를 감으면 1초마다 x만큼의 체력 회복
# t초 동안 연속으로 붕대를 감는 데 성공하면 y만큼의 체력을 추가 회복
# 최대 체력만큼 충전은 불가능
# 공격을 당하면 취소되고, 공격을 당하는 순간 최력 회복 불가능
# 공격 혹은 취소로 기술이 중지되면 즉시 붕대 감기를 사용하며, 연속 감기는 0으로 초기화
# 몬스터의 공격으로 체력이 0 이하가 되면 아웃
# 몬스터의 공격으로 죽는다면 -1을 반환
def solution(bandage, health, attacks):
    
    t = bandage[0]
    x = bandage[1]
    extra = bandage[2]
    max_health = health
    
    dick = { n[0]:n[1] for n in attacks}

    seq = 0
    
    for n in range(1, 1001):
        if n in dick:
            seq = 0
            health = health-dick[n]
            if health <= 0 :
                return -1
            del dick[n]
        
        else:
            seq += 1
            health += x
            if seq == t:
                health = health +extra
                seq = 0
        health = min(max_health, health)
        
        if len(dick) == 0:
            return health
        
    return health