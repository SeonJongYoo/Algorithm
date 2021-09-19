# DFS와 BFS

import sys
from collections import deque


def DFS(L, s):
    if L == n:
        return
    else:
        for i in range(1, n+1):
            if arr[s][i] == 1 and visit1[i] == 0:
                visit1[i] = 1
                res1.append(i)
                DFS(L+1, i)


n, m, v = map(int, sys.stdin.readline().rstrip().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a][b] = 1
    arr[b][a] = 1
visit1 = [0]*(n+1)
visit1[v] = 1
res1 = [v]
DFS(0, v)
for x in res1:
    print(x, end=" ")
print()


visit2 = [0]*(n+1)
Q = deque()
Q.append(v)
res2 = []
while Q:
    tmp = Q.popleft()
    if visit2[tmp] == 0:
        visit2[tmp] = 1
        res2.append(tmp)
    for k in range(1, n+1):
        if tmp == k:
            continue
        if arr[tmp][k] == 1 and visit2[k] == 0:
            Q.append(k)
for y in res2:
    print(y, end=" ")