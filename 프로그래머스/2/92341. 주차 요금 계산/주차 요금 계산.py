import math

def solution(fees, records):
    answer = {}

    _in_dict = {}
    
    for record in records:
        time, car, r_type = parse(record)
        if r_type == 'IN':
            _in_dict[car] = time
        else:
            elapsed = time - _in_dict[car]
            if car in answer:
                answer[car]+= elapsed
            else:
                answer[car] = elapsed
            del _in_dict[car]
        
    for key in _in_dict.keys():
        if key in answer:
            answer[key] += convert("23:59") - _in_dict[key]
        else:
            answer[key] = convert("23:59") - _in_dict[key]
    
    keys = sorted(answer.keys())
    ans = []
    
    for key in keys:
        agg = answer[key]
        ans.append(compute(fees, agg))
        
    return ans

def parse(record):
    records = record.split(" ")
    time = records[0]
    cat = records[1]
    r_type = records[2]
    
    return (convert(time), int(cat), r_type)

def convert(time):
    times = time.split(":")
    hour = int(times[0])
    miniute = int(times[1])
    
    return hour * 60 + miniute

def compute(fees, time):
    gibon = fees[0]
    gibon_fee = fees[1]
    dani = fees[2]
    dani_fee = fees[3]
        
    return gibon_fee+ max(0,(math.ceil((time - gibon) / dani))) * dani_fee