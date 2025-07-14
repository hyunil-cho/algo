def solution(phone_book):
    answer = True
    
    hash = dict()
    
    phone_book = sorted(phone_book, key=len, reverse=True)
    
    for next in phone_book:
        if next in hash:
            return False;
        for size in range(1, len(next)+1):
            val = next[:size]
            hash[val] = True
    
    return True