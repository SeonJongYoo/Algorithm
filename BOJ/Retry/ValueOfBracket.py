# 괄호의 값

import sys
s = list(sys.stdin.readline().rstrip())
stack = []
num = 1
res = 0
flag = False
for i in range(len(s)):
    if s[i] == '(':
        num *= 2
        stack.append(s[i])
    elif s[i] == '[':
        num *= 3
        stack.append(s[i])
    else:
        if s[i] == ')':
            if not stack:
                flag = True
                break
            else:
                tmp = stack.pop()
                if s[i-1] == '(':
                    res += num
                elif tmp == '[':
                    flag = True
                    break
                num //= 2
        elif s[i] == ']':
            if not stack:
                flag = True
                break
            else:
                tmp = stack.pop()
                if s[i-1] == '[':
                    res += num
                elif tmp == '(':
                    flag = True
                    break
                num //= 3
if flag or stack:
    print(0)
else:
    print(res)
