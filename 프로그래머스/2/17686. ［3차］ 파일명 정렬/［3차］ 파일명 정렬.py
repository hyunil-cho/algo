def solution(files):
    answer = []
    
    return sorted(files, key=sort_me, reverse=False)

def sort_me(s):
    
    head, number = decompse(s)
    return head.lower(), int(number)

def decompse(f):
    
    head, head_idx = getHead(f)
    number = getNumber(f[head_idx:])
    return head, number

def getNumber(file):
    number = []
    for idx, _n in enumerate(file):
        if idx < 5 and _n.isnumeric():
            number.append(_n)
        else:
            return "".join(number)
    return "".join(number)
    
def getHead(file):
    head = []
    for idx, _n in enumerate(file):
        if not _n.isnumeric():
            head.append(_n)
        else:
            return "".join(head), idx