def solution(numbers, target):
    
    def recursive(idx, cur_val,target):
        
        if idx == len(numbers):
            if cur_val == target:
                return 1
            return 0
        _sum = 0
        _sum += recursive(idx+1, cur_val + numbers[idx], target)
        _sum += recursive(idx+1, cur_val - numbers[idx], target)
        
        return _sum
        
    return recursive(0, 0, target)    
