# 스택
import sys
N = sys.stdin.readline()
stack = [0]*(int(N)+1)
top = -1
for _ in range(int(N)):
    s = sys.stdin.readline().rstrip()
    if "push" in s:
        tmp = s.split()
        top += 1
        stack[top] = int(tmp[1])
    elif s == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            stack[top] = 0
            top -= 1
    elif s == "size":
        print(top+1)
    elif s == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif s == "top":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
