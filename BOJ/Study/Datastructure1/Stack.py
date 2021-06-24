# 스택

import sys
n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
            tmp = stack[:len(stack)-1]
            stack = tmp
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])