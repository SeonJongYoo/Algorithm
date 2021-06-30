# 숨바꼭질 6

import sys


def getGCD(x, y):
    while y != 0:
        x, y = y, x%y
    return x


n, s = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
if n == 1:
    print(abs(A[0] - s))
else:
    dis = []
    for i in range(n):
        dis.append(abs(A[i] - s))
    Min = 1000000000
    res = dis[0]
    for i in range(1, n):
        res = getGCD(res, dis[i])
        if res < Min:
            Min = res
    print(Min)