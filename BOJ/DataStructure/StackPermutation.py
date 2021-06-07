# 스택 수열


# 1 ~ 8까지의 숫자들을 stack을 이용하여 입력과 같은 순서로 만들 수 있는지
n = int(input())
arr = [i for i in range(n, 0, -1)]
In = []
stack = []
for _ in range(n):
    In.append(int(input()))
i = 0
temp = 0
ans = []
flag = False
while stack or arr:
    if stack and stack[len(stack)-1] == In[i]:
        stack.pop()
        ans.append('-')
        i += 1
    elif arr:
        stack.append(arr.pop())
        ans.append('+')
    if temp == len(stack):
        flag = True
        break
    temp = len(stack)

if flag:
    print("NO")
else:
    for x in ans:
        print(x)