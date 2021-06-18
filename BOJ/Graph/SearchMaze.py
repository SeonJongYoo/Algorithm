# 미로 탐색


# 내가 작성한 코드 - DFS - 시간 초과
'''def DFS(L, x, y):
    global Min
    if L >= Min:
        return
    if x == n-1 and y == m-1:
        if L < Min:
            Min = L
    else:
        if board[x][y] == 1 and visit[x][y] != 0:
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1 and visit[xx][yy] == 0:
                    visit[xx][yy] = L+1
                    DFS(L+1, xx, yy)
                    visit[xx][yy] = 0


n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Min = 2147000000
visit[0][0] = 1
DFS(1, 0, 0)
print(Min)'''


# 내가 작성한 코드2 - BFS- 정답
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
visit[0][0] = 1
while Q:
    curr = Q.popleft()
    for i in range(4):
        xx = curr[0] + dx[i]
        yy = curr[1] + dy[i]
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1 and visit[xx][yy] == 0:
            visit[xx][yy] = visit[curr[0]][curr[1]]+1
            Q.append((xx, yy))
res = visit[n-1][m-1]
print(res)