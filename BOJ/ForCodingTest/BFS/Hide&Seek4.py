# 숨바꼭질 4


# 진행할 때마다 직전 위치를 기록해 놓는다!!!
import sys
from collections import deque


n, k = map(int, sys.stdin.readline().rstrip().split())
Q = deque()
visit = [-1]*100001
visit[n] = 0
Q.append(n)
path = [0]*100001  # 직전 위치 기록을 위한 리스트
while Q:
    size = len(Q)
    for _ in range(size):
        curr = Q.popleft()
        if curr == k:
            print(visit[k])
            res = []
            idx = k
            while idx != n:
                res.append(idx)
                idx = path[idx]
            print(n, end=" ")
            for i in range(len(res)-1, -1, -1):
                print(res[i], end=" ")
            sys.exit(0)
        x1 = curr - 1
        x2 = curr + 1
        x3 = curr * 2
        if 0 <= x1 < 100001 and visit[x1] == -1:
            visit[x1] = visit[curr] + 1
            Q.append(x1)
            path[x1] = curr
        if 0 <= x2 < 100001 and visit[x2] == -1:
            visit[x2] = visit[curr] + 1
            Q.append(x2)
            path[x2] = curr
        if 0 <= x3 < 100001 and visit[x3] == -1:
            visit[x3] = visit[curr] + 1
            Q.append(x3)
            path[x3] = curr
