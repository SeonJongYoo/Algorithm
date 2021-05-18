# 잃어버린 괄호

# 내가 작성한 코드
# 괄호를 한 번만 칠 수 있다고 생각했다.
# +-+-로 연산자가 반복적으로 나타난다는 조건을 놓쳤다.
# 모든 케이스에 대해서 괄호를 쳐서 연산을 수행하고 최종 결과가 최소인 값을 답으로 했다.
'''inp = list(map(str, input()))
exp = []
num = ""
for i in range(len(inp)):
    if inp[i] != '-' and inp[i] != '+':
        num += inp[i]
    else:
        exp.append(int(num))
        exp.append(inp[i])
        num = ""
exp.append(int(num))
if len(exp) == 1:
    res = exp[0]
else:
    res = 2147000000

for i in range(0, len(exp)-1, 2):
    tlist = []
    ch = [0] * len(exp)
    flag = False
    tmp = 0
    # 숫자 연산자 숫자 -> 총 3개씩 추출
    for j in range(i, i+3):
        ch[j] = 1
    if exp[i+1] == '-':
        tmp = exp[i] - exp[i+2]
    elif exp[i+1] == '+':
        tmp = exp[i] + exp[i+2]
    for j in range(len(exp)):
        if ch[j] == 0:
            tlist.append(exp[j])
        elif not flag and ch[j] == 1:
            tlist.append(tmp)
            flag = True
    for j in range(1, len(tlist), 2):
        if tlist[j] == '-':
            tlist[j+1] = tlist[j-1] - tlist[j+1]
        elif tlist[j] == '+':
            tlist[j+1] = tlist[j - 1] + tlist[j + 1]
        if len(tlist) < 3:
            break
    if tlist[len(tlist)-1] < res:
        res = tlist[len(tlist)-1]
print(res)'''


# 답을 확인하고 작성한 코드
# 괄호를 쳐서 주어진 식의 값이 최소가 되는 경우
# -> +연산을 미리하고 나중에 모두 -연산을 한다.
inp = input()
exp = inp.split("-")
res = []
for i in range(len(exp)):
    tmp = []
    tmp1 = 0
    tmp2 = 0
    if '+' not in exp[i]:
        tmp1+=int(exp[i])
        res.append(tmp1)
    else:
        tmp = exp[i].split('+')
        for j in range(len(tmp)):
            tmp2+=int(tmp[j])
        res.append(tmp2)
Min = 0
for i in range(len(res)):
    if i == 0:
        Min += res[i]
    else:
        Min -= res[i]
print(Min)