# 팩토리얼 0의 개수


import sys


def Fac(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * Fac(num-1)


n = int(sys.stdin.readline().rstrip())
res = Fac(n)
cnt = 0
while True:
    div = res % 10
    res //= 10
    if div == 0:
        cnt += 1
    else:
        break
print(cnt)