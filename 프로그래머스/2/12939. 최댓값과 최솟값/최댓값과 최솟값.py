def solution(s):
    answer = ''
    
    arr = s.split()
    arr = [int(x) for x in arr]
    arr.sort()
    
    print(arr)
    
    
    return str(arr[0])+" "+str(arr[-1])