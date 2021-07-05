# 날짜 계산


import sys

e, s, m = map(int, sys.stdin.readline().rstrip().split())
e1, s1, m1 = 1, 1, 1
res = 1
while True:
    if e1 == e and s1 == s and m1 == m:
        break
    e1 += 1
    if e1 > 15:
        e1 = 1
    s1 += 1
    if s1 > 28:
        s1 = 1
    m1 += 1
    if m1 > 19:
        m1 = 1
    res += 1
print(res)