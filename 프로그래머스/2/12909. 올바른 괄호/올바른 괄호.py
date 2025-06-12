def solution(s):
    
    stack = []
    
    
    for next in s:
        
        if len(stack) == 0:
            stack.append(next)
        elif next == ')' and stack[-1] =='(':
            stack.pop()
        else:
            stack.append(next)
    
    print(stack)
    return len(stack) == 0