def solution(prices):
    answer = [0 for i in range(0, len(prices))]
    
    _stack = []
    
    for idx, price in enumerate(prices):
        price = Price(idx, price)
        if not _stack:
            _stack.append(price)
        else:
            if (_stack[-1].compare(price)) == -1:
                _stack.append(price)
            else:
                while _stack and _stack[-1].compare(price) != -1:
                    removed_one = _stack.pop()
                    answer[removed_one.offset] = removed_one.compare(price)
                _stack.append(price)
                
    if _stack:
        top = _stack.pop()
        while _stack:
            _next = _stack.pop()
            answer[_next.offset] = top.offset - _next.offset
        
    
    return answer

class Price:
    def __init__(self, offset, value):
        self.offset = offset
        self.value = value
    def compare(self, price):
        if self.value <= price.value:
            return -1
        else:
            return price.offset - self.offset