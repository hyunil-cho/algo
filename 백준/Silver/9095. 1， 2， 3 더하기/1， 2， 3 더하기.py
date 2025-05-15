n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)

for next in arr:
    mem = [0] * (next+1)
    mem[0] = 1
    if next == 1 :
        print(1);
    elif next == 2 :
        print(2);
    else:
        mem[1] = 1
        mem[2] = 2
        
        for w in range(3, next+1):
            mem[w] = mem[w-1] + mem[w-2] + mem[w-3];
        print(mem[next])