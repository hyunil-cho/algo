def solution(players, callings):
    
    table = { value:idx for idx, value in enumerate(players)}
    
    for calling in callings:
        cur_position = table[calling]
        prev_position = cur_position - 1
        
        prev_name = players[prev_position]
        
        players[prev_position], players[cur_position] = players[cur_position], players[prev_position]
        table[calling] -= 1
        table[prev_name] += 1

    return [k for k, v in sorted(table.items(), key=lambda table: table[1])]
