def solution(s):
    length = len(s)
    is_even = length % 2 == 0
    
    if length == 1 or length == 2:
        return s;
    
    if is_even:
        return s[length//2-1 : length//2+1]
    else:
        return s[length//2];