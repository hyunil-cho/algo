def solution(s):
    parts = preprocessing(s)
    parts = sorted(parts, key=len, reverse=False)
    
    answer = []
    _set = set()
    
    for part in parts:
        for ele in part:
            if ele not in _set:
                answer.append(int(ele))
                _set.add(ele)
    
    return answer

def preprocessing(s):
    s = s[1:len(s)-1]
    parts = s.split('},{')
    parts[0] = parts[0][1:]
    parts[len(parts)-1] = parts[len(parts)-1][:-1]
    
    for idx in range(0, len(parts)):
        parts[idx] = parts[idx].split(",")
    
    return parts 