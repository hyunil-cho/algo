n = int(input())
arr = list(map(int,input().split()))
mem = [arr[i] for i in range(n)]

mem[0] = arr[0]

for idx, cur in enumerate(arr):
    for prev in range(0, idx):
        if arr[prev] >= cur:
            continue
        mem[idx] = max(mem[idx], mem[prev]+cur)

print(max(mem))
 