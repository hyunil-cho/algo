# N * (50 * 50 * 10)
def solution(mats, park):
    mats.sort()
    x_len = len(park)
    y_len = len(park[0])
    
    max_cnt = -1;
    for mat in mats:
        for x in range(x_len):
            for y in range(y_len):
                if park[x][y] != '-1':
                    continue;
                if x+(mat-1) >= x_len or y+(mat-1) >= y_len:
                    continue;
                is_okay = True;
                for nx in range(x, x+mat):
                    for ny in range(y, y+mat):
                        if park[nx][ny] != '-1':
                            is_okay = False
                            break;
                
                if is_okay:
                    max_cnt = max(max_cnt, mat);
    return max_cnt