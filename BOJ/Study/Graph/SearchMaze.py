# 미로 탐색

import sys
from collections import deque


n, m = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
Q = deque()
Q.append((0, 0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit[0][0] = 1
while Q:
    curr = Q.popleft()
    if maze[curr[0]][curr[1]] == 1 and visit[curr[0]][curr[1]] != 0:
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = visit[curr[0]][curr[1]] + 1
                Q.append((nx, ny))
print(visit[n-1][m-1])