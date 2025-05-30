n = int(input())

mem = [0 for _ in range(n+1)]
mem[1] = 1

for idx in range(2, n+1):
    mem[idx] = mem[idx-1] + mem[idx-2]
print(mem[n])