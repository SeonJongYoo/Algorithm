# 진법 변환

import sys
n, b = map(str, sys.stdin.readline().rstrip().split())
res = 0
b = int(b)
L = len(n)-1
for x in n:
    if ord(x) >= 65:
        tmp = (ord(x)-55) * pow(b, L)
    else:
        tmp = int(x) * pow(b, L)
    res += tmp
    L -= 1
print(res)