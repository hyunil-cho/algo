from collections import Counter

def solution(str1, str2):
    answer = 0
    arr1 = split(str1)
    arr2 = split(str2)
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    keys1 = list(count1.keys())
    keys2 = list(count2.keys())
    keys = keys1+keys2
    
    set_ = set()
    for key in keys:
        set_.add(key)
    
    commons = []
    sums = []
    
    for key in set_:
        val1 = count1[key]
        val2 = count2[key]
        
        if val1 >0 and val2 > 0:
            min_val = min(val1, val2)
            for _ in range(0, min_val):
                commons.append(key)
            max_val = max(val1, val2)
            for _ in range(0, max_val):
                sums.append(key)
        else:
            for _ in range(0, max(val1, val2)):
                sums.append(key)
    print(commons, sums)
    
    if len(sums) == 0 and len(commons) == 0:
        return 65536
    
    return int((len(commons) / len(sums)) * 65536)

def split(str):
    arr = []
    str = str.lower()
    for idx in range(0, len(str)-1, 1):
        val = str[idx:idx+2]
        if val.isalpha():
            arr.append(val)
 
    return arr