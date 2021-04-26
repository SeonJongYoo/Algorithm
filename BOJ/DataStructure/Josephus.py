# 요세푸스 문제
from collections import deque
n, k = map(int, input().split())
Q = []
for i in range(1, n+1):
    Q.append(i)
res = []
tk = k-1
tn = n
while Q:
    tmp = Q.pop(tk%tn)
    res.append(tmp)
    tn -= 1
    if tn == 0:
        continue
    tk += k-1
    tk %= tn
print("<", end="")
for i in range(n-1):
    print(res[i], end=", ")
print(res[n-1], end=">")