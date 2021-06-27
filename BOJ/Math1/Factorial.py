# 팩토리얼

import sys

def Fac(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return num * Fac(num-1)


n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(1)
else:
    res = Fac(n)
    print(res)