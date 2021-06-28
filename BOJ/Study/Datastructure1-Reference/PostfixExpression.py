# 후위표기식
# import sys
# exp = sys.stdin.readline().rstrip()
# stack1 = []  # operand
# stack2 = []  # operator
# for x in exp:
#     if ord(x) < 65:
#         if x == '*':
#             if stack1[-1] == '+' or stack1[-1] == '-':
#                 if stack2 and stack2[-1] == ')':
#                     continue
#                 tmp = stack1.pop()
#                 stack2.append(tmp)
#         elif x == '/':
#             if stack1[-1] == '+' or stack1[-1] == '-':
#                 if stack2 and stack2[-1] == ')':
#                     continue
#                 tmp = stack1.pop()
#                 stack2.append(tmp)
#         elif x == ')':
#             tmp = stack2.pop()
#             stack1.append(tmp)
#             continue
#         stack2.append(x)
#     else:
#         if stack1:
#             stack1.append(x)
#             tmp = stack2.pop()
#             if tmp != '(':
#                 stack1.append(tmp)
#         else:
#             stack1.append(x)
#     print(stack1)
#     print(stack2)
# for x in stack1:
#     print(x, end="")
# while stack2:
#     t = stack2.pop()
#     if t != '(' and t != ')':
#         print(t, end="")


# 내가 작성한 코드2 - 오답
# 괄호 처리가 제대로 되지 않음
# import sys
# exp = sys.stdin.readline().rstrip()
# stack1 = []  # operand
# stack2 = []  # operator
# for i in range(len(exp)):
#     print("stack1: ", stack1)
#     print("stack2: ", stack2)
#     if ord(exp[i]) < 65:
#         if (exp[i] == '*' or exp[i] == '/') and (stack1[-1] == '+' or stack1[-1] == '-'):
#             if stack2 and stack2[-1] == ')':
#                 stack2.append(exp[i])
#                 continue
#             tmp = stack1.pop()
#             stack2.append(tmp)
#         stack2.append(exp[i])
#     else:
#         stack1.append(exp[i])
#         while stack2:
#             tmp = stack2.pop()
#             if tmp == '(' or tmp == ')':
#                 stack2.append(tmp)
#                 break
#             stack1.append(tmp)
# for x in stack1:
#     print(x, end="")
# while stack2:
#     tmp = stack2.pop()
#     if tmp == '(' or tmp == ')':
#         continue
#     print(tmp, end="")


# 정답 코드
import sys
exp = sys.stdin.readline().rstrip()
stack = []
for i in range(len(exp)):
    if 64 < ord(exp[i]) < 91:
        print(exp[i], end="")
    else:
        if exp[i] == '(':
            stack.append(exp[i])
        elif exp[i] == '*' or exp[i] == '/':  # 연산자 우선순위: 같은 우선순위의 연산자를 만나면 stack에서 pop한다.
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack[-1], end="")
                stack.pop()
            stack.append(exp[i])
        elif exp[i] == '+' or exp[i] == '-':  # +와 -는 우선순위가 가장 낮으므로 stack 비거나 열린 괄호를 만날 때까지 stack에서 pop한다.
            while stack and stack[-1] != '(':
                print(stack[-1], end="")
                stack.pop()
            stack.append(exp[i])
        elif exp[i] == ')':  # 열린 괄호를 만날 때까지 연산자들을 stack에서 모두 pop!
            while stack and stack[-1] != '(':
                print(stack[-1], end="")
                stack.pop()
            stack.pop()
while stack:
    print(stack[-1], end="")
    stack.pop()