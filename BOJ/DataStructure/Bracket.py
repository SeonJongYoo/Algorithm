# 괄호
import sys
t = sys.stdin.readline()
for _ in range(int(t)):
    ps = sys.stdin.readline().rstrip()
    stack = []
    top = -1
    for i in range(len(ps)):
        if top != -1 and stack[top] == '(' and stack[top] != ps[i]:
            stack.pop()
            top -= 1
            continue
        stack.append(ps[i])
        top += 1
    if top == -1:
        print("YES")
    else:
        print("NO")