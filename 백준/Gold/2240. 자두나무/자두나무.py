T,W = input().split(" ")
T,W = int(T), int(W)

times = []

for _ in range(T):
  times.append(int(input()))

mem = [[0 for _ in range(W+1)] for _ in range(T+1)]

       
for next in range(1, T+1):
  tree_val = times[next-1]
  for w in range(W+1):
    if w == 0:
      mem[next][w] = mem[next-1][w]
    else:
      mem[next][w] = max(mem[next-1][w], mem[next-1][w-1])
    cur_pos = 1 if w % 2 == 0 else 2
    if cur_pos == tree_val:
        mem[next][w] += 1

print(max(mem[T]))
  