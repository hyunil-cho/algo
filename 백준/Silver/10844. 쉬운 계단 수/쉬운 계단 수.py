n = int(input())
mem = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1,10):
    mem[1][i] = 1
    
remain = 1000000000

for idx in range(2,n+1):
    for end_num in range(0, 10):
        if end_num == 0:
            mem[idx][0] = mem[idx-1][1] % remain
        elif end_num < 9:
            mem[idx][end_num] = (mem[idx-1][end_num-1]%remain + mem[idx-1][end_num+1]%remain) % remain
        elif end_num == 9:
            mem[idx][9] = mem[idx-1][8] % remain
res = 0
for val in mem[n]:
    res += val

print(res % remain)