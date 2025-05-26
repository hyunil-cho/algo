def get_distance(from_pos, to_pos):
    return abs(from_pos[0] - to_pos[0]) + abs(from_pos[1] - to_pos[1])
    
def get_position(val):
    remain = (val-1) % 3
    if val ==0:
        return [3,1]
    if val <= 3: 
        return [0, remain]
    elif val <= 6:
        return [1, remain]
    else:
        return [2,remain]
    
    
def solution(numbers, hand):
    
    left = [3,0]
    right = [3,2]
    
    answer = []
    
    for num in numbers:
        num_position = get_position(num)
        if num in [1,4,7]:
            left = num_position
            answer.append("L")
        elif num in [3,6,9]:
            right = num_position
            answer.append("R")
        else:
            dis_from_left = get_distance(left, num_position)
            dis_from_right = get_distance(right, num_position)
            
            if dis_from_left == dis_from_right:
                if hand =='right':
                    right = num_position
                    answer.append("R")
                else :
                    left = num_position
                    answer.append("L")
            else :
                if dis_from_left > dis_from_right:
                    right = num_position
                    answer.append("R")
                else:
                    left = num_position
                    answer.append("L")      
    return ''.join(answer)