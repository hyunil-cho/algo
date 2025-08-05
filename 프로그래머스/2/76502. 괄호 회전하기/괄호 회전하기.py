def solution(s):
    answer = 0
    
    for cnt in range(0, len(s)):
        cur_val = move(s, cnt)
        if isValid(cur_val):
            answer+=1

    return answer

def isValid(s):
    
    _stack = []
    
    for _next in s:
        if not _stack:
            _stack.append(_next)
        else:
            top = _stack[-1];
            if _next == ')' and top =='(':
                _stack.pop()
            elif _next =='}' and top == '{':
                _stack.pop()
            elif _next ==']' and top =='[':
                _stack.pop()
            else:
                _stack.append(_next)
                    
    return True if not _stack else False

def move(s, cnt):
    return s[cnt:len(s)]+s[0:cnt]