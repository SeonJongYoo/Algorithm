# 쇠막대기

line = list(map(str, input()))
stack = [line[0]]
top = 0
cnt = 1
res = 0
for i in range(1, len(line)):
    if top > -1 and line[i] != stack[top]:
        stack.pop()
        top -= 1
        if line[i] != line[i-1]:
            cnt -= 1
            res += cnt
            continue
        cnt -= 1
        res += 1
    else:
        stack.append(line[i])
        cnt += 1
        top += 1
print(res)