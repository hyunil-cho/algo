size = int(input())
arr = []
for _ in range(size):
  next_line = list(map(int ,input().split()))
  arr.append(next_line)

mem = [[0] * x for x in range(1, size+1)]

mem[0][0] = arr[0][0]
for nx in range(1, size):
  for idx, val in enumerate(arr[nx]):
    if idx == 0:
        mem[nx][0] = mem[nx-1][0] + arr[nx][0]
    elif idx == len(arr[nx])-1:
        mem[nx][idx] = mem[nx-1][idx-1] + arr[nx][idx]
    else:
        mem[nx][idx] = max(mem[nx-1][idx-1], mem[nx-1][idx]) + arr[nx][idx]

print(max(mem[size-1]))
          
