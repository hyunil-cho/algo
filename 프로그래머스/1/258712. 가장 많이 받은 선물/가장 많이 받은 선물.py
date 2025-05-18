# 두 사람 사이에 선물을 주고받은 기록이 있다면, 이번달까지 더 많은 선물을 준 사람이 다음 달 선물을 받는다
# 선물을 주고받은 기록이 없거나, 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 받는다
## 선물 지수란, 친구들에게 준 선물의 선에서, 받은 선물의 수를 뺀 값이다.
# 이때, 가장 많은 선물을 받을 사람은?


def solution(friends, gifts):
    
    # 선물을 주고 받은 N*N 행령을 생성 및 초기화
    # 선물 지수를 계산
    # 친구 목록을 돌면서, 선물 수를 계산하고, MAX 선물 수를 리턴
    
    length = len(friends)
    index = { val : idx  for idx, val in enumerate(friends) }
    metric = [[0] * length for _ in range(length)]
    indicator = { f:0 for f,_ in enumerate(friends) }
    
    for gift in gifts:
        _from, _to = gift.split()
        indicator[index[_from]]+=1
        indicator[index[_to]]-=1
        metric[index[_from]][index[_to]] += 1
    
    max_val = 0;
    for from_idx, _ in enumerate(friends):
        cnt = 0;
        for to_idx, _ in enumerate(friends):
            if from_idx == to_idx:
                continue
            else:
                if metric[from_idx][to_idx] > metric[to_idx][from_idx]:
                    cnt+=1;
                elif metric[from_idx][to_idx] == metric[to_idx][from_idx]:
                    if indicator[from_idx] > indicator[to_idx]:
                        cnt+=1;
        max_val = max(max_val, cnt)
    return max_val