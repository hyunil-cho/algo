# 10 50 50 90
# 50 50 70 80 => 3
def solution(people, limit):
    answer = 0
    
    people.sort()
    
    right_idx = len(people)-1
    left_idx = 0

    while left_idx <= right_idx:
        max_person = people[right_idx]
        min_person = people[left_idx]
        answer+=1
        if max_person + min_person <= limit:
           left_idx  += 1
           right_idx -=1
        else:
            right_idx -= 1
           
    return answer