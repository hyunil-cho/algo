pram = list(map(int,input().split()))
arr = list(map(int, input().split()))

ranges = []

for _ in range(pram[1]):
    ranges.append(list(map(int, (input().split()))))

sum = [0] * (len(arr))

sum[0] = arr[0]

for next in range(1, len(arr)):
    sum[next] = sum[next-1]+arr[next]
    
for range in ranges:
    range[0] = range[0] -1;
    range[1] = range[1] -1;
    
    if range[0] == range[1] : print(arr[range[0]])
    elif range[0] == 0:
        print(sum[range[1]])
    else:
        print(sum[range[1]]-  sum[range[0]-1])
