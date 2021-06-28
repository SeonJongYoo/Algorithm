# 최소공배수

import sys

# 최대공약수 - 유클리드 호제법
def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    res = GCD(a, b)
    r1 = a//res
    r2 = b//res
    print(res*r1*r2)