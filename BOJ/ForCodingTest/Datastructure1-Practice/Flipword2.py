# 단어 뒤집기

import sys
#from collections import deque
s = sys.stdin.readline().rstrip()
stack = []
#Q = deque()
for x in s:
    if x == ' ' and stack:
        if '<' not in stack:
            while stack:
                tmp = stack.pop()
                print(tmp, end="")
            print(' ', end="")
        else:
            stack.append('A')
    elif x == '>' and stack:
        stack.append(x)
        stack = stack[::-1]
        while stack:
            tmp = stack.pop()
            if tmp == 'A':
                print(' ', end="")
            else:
                print(tmp, end="")
    elif x == '<' and stack:
        while stack:
            tmp = stack.pop()
            print(tmp, end="")
        stack.append(x)
    else:
        stack.append(x)
if stack:
    while stack:
        tmp = stack.pop()
        print(tmp, end="")