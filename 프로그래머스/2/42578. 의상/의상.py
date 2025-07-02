def solution(clothes):
    answer = 0
    dict = {}
    
    
    for next in clothes:
        kind = next[1]
        name = next[0]
        
        if kind in dict:
            dict[kind].append(name)
        else:
            new_arr = [name]
            dict[kind] = new_arr
    
    temp = 1
    for key in dict.keys():
        temp = temp * (len(dict[key])+1)
        
    
    
    return temp-1