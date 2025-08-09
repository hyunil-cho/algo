# 보조 컨테이너는 stack(가장 마지막에 넣은 것부터 꺼낼 수 있다,)
def solution(order):
    
    containers = [next for next in range(1, len(order)+1)]
    
    _stack = []
    
    next_idx = 0
    
    for c in containers:
        while _stack and _stack[-1] == order[next_idx]:
            _stack.pop()
            next_idx += 1
        if c == order[next_idx]:
            next_idx += 1
        else:
            _stack.append(c)
            

    while _stack and _stack[-1] == order[next_idx]:
        _stack.pop()
        next_idx += 1            
    
    return max(next_idx,0)