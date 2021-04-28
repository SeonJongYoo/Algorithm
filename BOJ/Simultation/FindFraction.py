# 분수찾기

x = int(input())
flag = False
cnt = 1
rcnt = 0
y = 1
if x > 1:
    for i in range(2, 10000):
        if cnt > x:
            break
        if cnt <= x:
            rcnt = cnt
            y = i
        if i%2 == 0:
            cnt += 1
        else:
            cnt = cnt + i + (i-2)
    res1 = 0
    res2 = 0
    if x > rcnt + (y - 2):
        rcnt += (y-1)*2
        y += 1

    res1 = 1 + abs(rcnt-x)
    res2 = (y-1) - abs(rcnt-x)

    print(res1, end="")
    print("/", end="")
    print(res2)
else:
    print(1, end="")
    print("/", end="")
    print(1)
