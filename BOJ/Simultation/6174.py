# 6174
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    m = n
    while m != 6174:
        tmp = []
        if m == 6174:
            break
        while m != 0:
            tmp.append(m%10)
            m = m // 10
        if len(tmp) < 4:
            tmp.append(0)
        tmp.sort()
        x1 = ""
        for i in range(len(tmp)):
            x1 += str(tmp[i])
        tmp.sort(reverse=True)
        x2 = ""
        for i in range(len(tmp)):
            x2 += str(tmp[i])
        m = int(x2) - int(x1)
        cnt += 1
    print(cnt)