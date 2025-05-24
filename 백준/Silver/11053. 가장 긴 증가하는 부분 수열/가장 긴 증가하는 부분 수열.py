n = int(input())
arr = list(map(int,input().split()))
mem = [1 for _ in range(n)]

for idx in range(n):
    for prev in range(0, idx):
        if arr[prev] >= arr[idx]:
            continue
        mem[idx] = max(mem[idx], mem[prev]+1)
print(max(mem))