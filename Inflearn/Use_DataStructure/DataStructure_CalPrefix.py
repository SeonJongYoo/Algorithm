# 후위식 연산

# 내가 작성한 코드
# 연산자를 만나면 stack의 top에서부터 두개의 숫자를 pop하여 연산!
a = input()
stack = []
res = 0
for x in a:
    if x.isdecimal():  # 숫자를 만나면 stack에 push!
        stack.append(int(x))
    else:
        if x == '+':
            res = stack.pop()
            res += stack.pop()
            stack.append(res)  # 연산 결과를 다시 stack에 push!
        elif x == '-':
            res = stack.pop()
            res -= stack.pop()
            res = -res
            stack.append(res)
        elif x == '*':
            res = stack.pop()
            res *= stack.pop()
            stack.append(res)
        elif x == '/':
            res = stack.pop()
            res /= stack.pop()
            stack.append(res)
print(res)

# 강의 코드
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:  # 나중에 pop한 것(n2)이 연산자 앞에 온다!
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)
print(stack[0])
