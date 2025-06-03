# 코드번호, 제조일, 최대수량, 현재수량
# sort_by를 기준으로, 오름차순 정렬
def solution(data, ext, val_ext, sort_by):
    
    index = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    answer = []
    for next in data:
        idx = index[ext]
        val = next[idx]
        if val < val_ext:
            answer.append(next)
    
    answer.sort(key=lambda key : key[index[sort_by]])

    return answer