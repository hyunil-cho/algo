def solution(my_string):
    answer = ""
    for idx in range(len(my_string)-1, -1, -1):
        answer += my_string[idx]

    return answer