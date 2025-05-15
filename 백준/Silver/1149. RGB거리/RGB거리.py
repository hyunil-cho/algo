n = int(input())
arr = []
for _ in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)
arr = list(arr)
memory = [[0] * (3), [0] * (3), [0] * (3)] * n

memory[0][0], memory[0][1], memory[0][2] = arr[0][0], arr[0][1], arr[0][2]

for next in range(1, n):
    memory[next][0] = min(memory[next-1][1],memory[next-1][2]) + arr[next][0]
    memory[next][1] = min(memory[next-1][0],memory[next-1][2]) + arr[next][1]
    memory[next][2] = min(memory[next-1][0],memory[next-1][1]) + arr[next][2]

print(min(memory[n-1]))