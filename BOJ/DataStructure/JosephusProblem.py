# 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
Q = deque(arr)
res = []
while Q:
    cnt = k
    while cnt > 1:
        if Q:
            tmp = Q.popleft()
            Q.append(tmp)
        cnt-=1
    res.append(Q.popleft())
print("<", end="")
for i in range(len(res)):
    print(res[i], end="")
    if i != len(res)-1:
        print(", ", end="")
print(">")