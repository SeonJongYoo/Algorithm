# 괄호
import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    bracket = sys.stdin.readline().rstrip()
    stack = []
    for b in bracket:
        if stack and b == ')':
            if stack[len(stack)-1] == '(':
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)
    if stack:
        print("NO")
    else:
        print("YES")