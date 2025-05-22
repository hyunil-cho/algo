def solution(food):
    
    temp = ''
    for idx in range(1, len(food)):
        num_food = food[idx] // 2
        if num_food > 0:
            temp = temp + str(idx) * num_food
    answer = temp + "0" + temp[::-1];
    
    return answer