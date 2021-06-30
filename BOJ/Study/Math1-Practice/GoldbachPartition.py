# 골드바흐 파티션

import sys

ck = [0] * 1000001
ck[1] = 1
num = 1000000
m = int(num**0.5)
for i in range(2, m+1):
    if ck[i]: continue
    for j in range(i + i, num+1, i):
        ck[j] = 1

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cnt = 0
    if n == 4:
        print(1)
    else:
        for x in range(3, n // 2 + 1, 2):
            if ck[x] == 0 and ck[n - x] == 0:
                cnt += 1
        print(cnt)
