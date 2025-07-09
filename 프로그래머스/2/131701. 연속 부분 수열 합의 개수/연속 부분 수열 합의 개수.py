def solution(elements):
    answer = 0
    
    datas = set()
    length = len(elements)
    
    arr = elements + elements
    
    for next in range(1, length+1):
        cur_val = 0
        
        for idx in range(0, length):
            total_idx = idx + next
            if total_idx <= len(arr):
                datas.add(sum(arr[idx : total_idx]))
    return len(datas)