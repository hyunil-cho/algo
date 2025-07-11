def solution(k, dungeons):
    max_val = 0
    def dfs(cur_k, cur_cnt, dungeons, history):
        nonlocal  max_val
        max_val = max(max_val, cur_cnt)
        for next in range(0, len(dungeons)):
            if history[next] == False:
                dungeon = dungeons[next]
                if dungeon[0] <= cur_k:
                    history[next] = True
                    dfs(cur_k-dungeon[1], cur_cnt+1, dungeons, history)
                    history[next] = False
    max_val = 0
    dfs(k, 0, dungeons, [False for _ in range(0, len(dungeons))])
                
        

    return max_val