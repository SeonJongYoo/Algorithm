# 에디터
import sys
editor = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(m):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'P':
        editor.append(command[1])
    elif command[0] == 'L':
        if editor:
            tmp = editor.pop()
            stack.append(tmp)
    elif command[0] == 'D':
        if stack:
            tmp = stack.pop()
            editor.append(tmp)
    else:
        if editor:
            editor.pop()
for x in editor:
    print(x, end="")
for x in stack[::-1]:
    print(x, end="")