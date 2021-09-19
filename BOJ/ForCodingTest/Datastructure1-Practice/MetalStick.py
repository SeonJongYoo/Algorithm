# 쇠막대기

import sys
bracket = list(sys.stdin.readline().rstrip())
stack = []
res = 0
cnt = 0
for i in range(len(bracket)):
    if stack and bracket[i] == ')':
        stack.pop()
        if bracket[i-1] == '(':
            cnt -= 1
            res += cnt
        else:
            cnt -= 1
            res += 1
    else:
        stack.append(bracket[i])
        cnt += 1
print(res)