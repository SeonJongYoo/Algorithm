# 카드 2
from collections import deque

n = int(input())
Q = deque()
for i in range(1, n+1):
    Q.append(i)
while len(Q) != 1:
    rest = Q.popleft()
    first = Q.popleft()
    Q.append(first)
print(Q[0])
