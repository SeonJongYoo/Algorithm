# 가장 큰 수

# 강의 코드
num, m = map(int, input().split())
# int형으로 입력받은 num을 string으로 변경 후, num의 원소 하나하나를 다시 int형으로 변경하면서 list에 저장한다.
num = list(map(int, str(num)))
stack = []
for x in num:
    # stack이 비어있지 않고 m(지우는 횟수)이 0보다 크고 stack 저장된 맨 뒤의 숫자가 현재 읽은 숫자보다 작으면 그 숫자를 pop!
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]  # stack의 맨 앞에서 부터 -m 앞까지를 출력
res = ''.join(map(str, stack))  # stack의 각 원소들을 string으로 변경하고 join함수로 합친다.
print(res)