# 삭제 순서에 따라 결과가 달라지는가?
# abba abbba ddffddeff eddeeeff
def solution(s):
    stack = []

    for next in s:
        if not stack:
            stack.append(next)
        else:
            if stack[-1] == next:
                stack.pop()
            else:
                stack.append(next)
    return 1 if len(stack) == 0 else 0