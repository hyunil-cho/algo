def solution(board, moves):
    answer = 0
    
    stack = []
    
    moves = [move - 1 for move in moves]
    
    for col in moves:
        for row in range(0, len(board)):
            value = board[row][col]
            board[row][col] = 0
            if value != 0 :
                if stack and stack[-1] == value:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(value)
                break
                
            
    
    return answer