1
2
3
4
5
def solution(n):
    pivot = n & -n;
    before = ((n ^ (n + pivot)) // pivot) >> 2;
    return (n + pivot) | before;
