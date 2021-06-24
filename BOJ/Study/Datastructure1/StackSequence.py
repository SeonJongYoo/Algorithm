# 스택 수열

import sys
n = int(sys.stdin.readline().rstrip())
stack = []
res = []
tmp = 1
flag = False
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if flag:
        break
    while True:
        if tmp > num:
            break
        res.append('+')
        stack.append(tmp)
        tmp += 1
    while True:
        if not stack:
            flag = True
            break
        res.append('-')
        x = stack.pop()
        if x == num:
            break
if not flag:
    for i in res:
        print(i)
else:
    print("NO")