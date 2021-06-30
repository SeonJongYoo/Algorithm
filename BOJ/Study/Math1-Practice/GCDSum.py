# GCD 합(최대 공약수)

# itertools 라이브러리 사용
# import itertools as it
# import sys
#
#
# def getGCD(x, y):
#     while y != 0:
#         x, y = y, x%y
#     return x
#
#
# t = int(sys.stdin.readline().rstrip())
# for _ in range(t):
#     num = list(map(int, sys.stdin.readline().rstrip().split()))
#     peer = it.combinations(num[1:], 2)
#     res = 0
#     for p in peer:
#         res += getGCD(p[0], p[1])
#     print(res)


# 이중 for문 사용 - itertools 라이브러리 보다 빠름
import sys


def getGCD(x, y):
    while y != 0:
        x, y = y, x%y
    return x


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    res = 0
    for i in range(1, num[0]):
        for j in range(i+1, num[0]+1):
            res += getGCD(num[i], num[j])
    print(res)