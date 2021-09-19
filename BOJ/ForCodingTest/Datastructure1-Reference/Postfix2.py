# 후위표기식

import sys
n = int(sys.stdin.readline().rstrip())
exp = list(sys.stdin.readline().rstrip())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline().rstrip()))
stack = []
for x in exp:
    if ord(x) < 65:
        op1 = stack.pop()
        op2 = stack.pop()
        if x == '+':
            stack.append(op2 + op1)
        elif x == '-':
            stack.append(op2 - op1)
        elif x == '*':
            stack.append(op2 * op1)
        elif x == '/':
            stack.append(op2 / op1)
    else:
        stack.append(num[ord(x)-65])
res = stack.pop()
print(format(res, ".2f"))