import sys

n = int(input())
arr = []
for _ in range(n):
    next = int(sys.stdin.readline())
    arr.append(next)

max_cnt = max(arr)

mem = [0 for _ in range(max_cnt+1)]
mem[0] = 1
mem[1] = 1

remain =  1_000_000_009
for next in range(2, max_cnt+1):
    if next-1 >= 0:
        mem[next] += mem[next-1]%remain
    if next-2 >= 0:
        mem[next] += mem[next-2]%remain
    if next-3 >= 0:
        mem[next] += mem[next-3]%remain
    mem[next] = mem[next] % remain
    
for next in arr:
    print(mem[next] % remain)
