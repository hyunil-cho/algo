def solution(wallet, bill):
    answer = 0
    def change(bill):
        bill[0], bill[1] = bill[1], bill[0]
    
    def fold(bill):
        idx = 0 if bill[0] > bill[1] else 1
        bill[idx] = bill[idx] // 2
    
    def is_okay(wallet, bill):
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            return True
        change(bill)
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            return True
        
        return False
    
    for cnt in range(1,100):
        if is_okay(wallet, bill):
            return cnt-1;
        fold(bill)
        
    
    return answer