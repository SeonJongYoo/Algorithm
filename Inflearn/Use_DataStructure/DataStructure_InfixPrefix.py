# 후위표기식 만들기

# 연산자를 만나면 stack에 push! - 이때, stack의 top보다 연산자 우선순위가 높으면 stack에 push!
# stack의 top보다 연산자 우선순위가 낮으면 stack에서 top을 pop하고 자기 자신을 push
# 여는 괄호는 무조건 append! - 닫는 괄호를 만나면 여는 괄호 사이에 있는 모든 연산자들을 pop!
# 여는 괄호 직후에 나오는 연산자는 append하고 이후에 들어오는 연산자는 우선순위를 비교하여 pop할지 결정
# 숫자를 만나면 그대로 출력!
# 입력 받은 중위표기식을 모두 읽고나면 stack을 모두 pop!

# 강의 코드
a = input()
stack = []
res=''
for x in a:
    if x.isdecimal():  # 10진수 숫자(0~9)인지 판단
        res += x
    else:  # stack[-1]은 top을 나타냄
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':  # 괄호 안에 있던 +와 - 연산
                res += stack.pop()
            stack.append(x)
        elif x == ')':  # 닫는 괄호를 만났을 때
            while stack and stack[-1] != '(':  # stack의 top이 연산자이면 모두 pop!
                res += stack.pop()
            stack.pop()
while stack:  # 중위표기식을 모두 읽고나서 stack에 남아있는 모든 연산자를 pop
    res += stack.pop()
print(res)