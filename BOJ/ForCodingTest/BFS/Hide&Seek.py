# 숨바꼭질

import sys
from collections import deque


n, k = map(int, sys.stdin.readline().rstrip().split())
Q = deque()
visit = [0]*100001
visit[n] = 1
Q.append(n)
while Q:
    size = len(Q)
    for _ in range(size):
        curr = Q.popleft()
        if curr == k:
            #print(visit)
            print(visit[k]-1)
            sys.exit(0)
        x1 = curr - 1
        x2 = curr + 1
        x3 = curr * 2
        if 0 <= x1 < 100001 and visit[x1] == 0:
            visit[x1] = visit[curr] + 1
            Q.append(x1)
        if 0 <= x2 < 100001 and visit[x2] == 0:
            visit[x2] = visit[curr] + 1
            Q.append(x2)
        if 0 <= x3 < 100001 and visit[x3] == 0:
            visit[x3] = visit[curr] + 1
            Q.append(x3)
