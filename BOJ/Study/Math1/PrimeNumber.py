# 소수

import sys
n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
ck = [0]*1001
ck[1] = 1
for i in range(2, 1000):
    for j in range(i*i, 1001, i):
        if ck[j] == 0:
            ck[j] = 1
res = 0
for i in num:
    if ck[i] == 0:
       res += 1
print(res)