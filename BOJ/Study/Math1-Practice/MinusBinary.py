# -2진수

import sys


def toBin(N):
    res = ""
    while N != 0:
        re = N % 2
        N //= -2
        res += str(re)
    return res[::-1]


n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)
else:
    ans = toBin(-n)
    print(ans)


