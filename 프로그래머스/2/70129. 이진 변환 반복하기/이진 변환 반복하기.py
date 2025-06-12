def solution(s):
    
    cnt = 0
    sum = 0
    
    while s != "1":
        sum += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt+=1
     
    return [cnt, sum]