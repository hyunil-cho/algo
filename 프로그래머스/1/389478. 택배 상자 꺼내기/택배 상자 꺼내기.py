# 홀수번째 층의 경우에는 정방향(왼쪽부터 오른쪽으로 가면서 값이 커짐)
# 짝수번째 층의 경우에는 역방향(왼족부터 오른쪽으로 가면서 값이 작아짐)
# 홀수번째 층끼리는 열이 같을 경우 2*w 만큼 차이남
# 짝수번재 층끼리는 열이 같을 경우 2*w 만큼 차이남

def solution(n, w, num):
    arr = [i for i in range(1, n+1)]
    stacks = [[] for i in range(w)]
    
    mode = True
    for start in range(0, n, w):
        next = arr[start : start+w]
        for idx, ele in enumerate(next):
            if mode:
                stacks[idx].append(ele)
            else:
                stacks[-1*(idx+1)].append(ele)
        mode = not mode
    
    for stack in stacks:
        cnt = 0;
        stack.reverse();
        for ele in stack:
            cnt+=1
            if ele == num:
                return cnt;
            
    