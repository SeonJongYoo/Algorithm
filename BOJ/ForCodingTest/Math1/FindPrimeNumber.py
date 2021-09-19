# 소수 구하기

import sys
m, n = map(int, sys.stdin.readline().rstrip().split())
ck = [0]*1000001
ck[1] = 1
for i in range(2, 1000000):
    for j in range(i*i, 1000001, i):
        if ck[j] == 0:
            ck[j] = 1
for i in range(m, n+1):
    if ck[i] == 0:
       print(i)