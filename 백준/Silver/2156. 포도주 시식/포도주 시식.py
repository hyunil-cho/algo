N = int(input())
arr = [0]

for _ in range(N):
  arr.append(int(input()))

mem = [[0,0] for _ in range(N+1)]

mem[1][0], mem[1][1] = arr[1], arr[1]

for n in range(2, N+1):
    mem[n][0] = max(mem[n-1][0], mem[n-1][1] + arr[n])
    mem[n][1] = arr[n] + max(mem[n-2])

print(max(mem[N]))