# Base Conversion

import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
n = list(map(int, sys.stdin.readline().rstrip().split()))
ten = 0
res = []
for x in n:
    ten += x * pow(a, m-1)
    m -= 1
while ten != 0:
    re = ten%b
    ten //= b
    res.append(re)
res.reverse()
for x in res:
    print(x, end=" ")