# 수 이어 쓰기 1

import sys

n = int(sys.stdin.readline().rstrip())
if n < 10:
    print(n)
else:
    size = len(str(n))
    tmp = 1
    Sum = 0
    while tmp < size:
        Sum += tmp*(pow(10, tmp) - pow(10, tmp-1))
        tmp += 1
    res = Sum + size*(n-pow(10, size-1)+1)
    print(res)