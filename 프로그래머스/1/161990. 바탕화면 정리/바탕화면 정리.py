# 최대 크기 => 50 * 50
# ".#..."
# "..#.."
# "...#."
# (0 1) -> (1,2)
def solution(wallpaper):
    wallpaper.append("." *len(wallpaper[0]))
    wallpaper = [next +"." for next in wallpaper]
    
    positions = []
    for x, n in enumerate(wallpaper):
        for y, nc in enumerate(n):
            if nc =='#':
                positions.append((x,y))
    
    min_val = 100000000
    res = []
    
    for x in range(len(wallpaper)-1):
        for y in range(len(wallpaper[0])-1):
            for nx in range(x+1, len(wallpaper)):
                for ny in range(y+1, len(wallpaper[0])):
                    is_okay = True                    
                    for position in positions:
                        tx = position[0]
                        ty = position[1]
                        
                        if not (tx >=x and tx<nx and ty >= y and ty< ny):
                            is_okay = False
                            break;
                    if is_okay:
                        cur_val = abs(nx-x) + abs(ny-y)
                        if cur_val < min_val:
                            min_val = cur_val
                            res = [x,y, nx, ny]
                        
    
    return res