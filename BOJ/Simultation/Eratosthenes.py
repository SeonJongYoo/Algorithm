# 에라토스테네스의 체

n, k = map(int, input().split())
ch = [0]*(n+1)
cnt = 0
res = 0
for i in range(2, n+1):
    if not ch[i]:
        cnt += 1
        ch[i] = cnt
        for j in range(i*i, n+1, i):
            if ch[j] == 0:
                cnt += 1
                ch[j] = cnt
for i in range(2, n+1):
    if ch[i] == k:
        print(i)
        break