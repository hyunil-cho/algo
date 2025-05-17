mem = [[0, 0] for _ in range(41)]
mem[0][0] = 1;
mem[0][1] = 0;
mem[1][0] = 0;
mem[1][1] = 1;

def sol(n):
  if n < 2:
    return (mem[n][0], mem[n][1])
  
  if mem[n][0] !=0 and mem[n][1] != 0:
      return (mem[n][0], mem[n][1]);
  
  for next in range(2, n+1):
    mem[next][0] = mem[next-1][0] + mem[next-2][0]
    mem[next][1] = mem[next-1][1] + mem[next-2][1]
  return (mem[next][0], mem[next][1])

nums = int(input())

arr = []
for _ in range(nums):
    next = int(input())
    res = sol(next);
    arr.append([res[0], res[1]])

for next in arr:
    print(next[0], next[1])