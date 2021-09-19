# 토마토

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
Q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visit[i][j] == 0:
            Q.append((i, j))
            visit[i][j] = 1
        if board[i][j] == -1:
            visit[i][j] = -1
while Q:
    tmp = Q.popleft()
    if visit[tmp[0]][tmp[1]] != 0:
        for k in range(4):
            xx = tmp[0] + dx[k]
            yy = tmp[1] + dy[k]
            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 0 and visit[xx][yy] == 0:
                visit[xx][yy] = visit[tmp[0]][tmp[1]] + 1
                Q.append((xx, yy))
day = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            print(-1)
            sys.exit(0)
        if day < visit[i][j]:
            day = visit[i][j]
print(day-1)