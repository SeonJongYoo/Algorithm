
# 단지 번호 붙이기


# 내가 작성한 코드
from collections import deque
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
L = 1
res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visit[i][j] == 0:
            cnt = 1
            visit[i][j] = L
            Q.append((i, j))
            while Q:
                c = Q.popleft()
                for k in range(4):
                    xx = c[0] + dx[k]
                    yy = c[1] + dy[k]
                    if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1 and visit[xx][yy] == 0:
                        visit[xx][yy] = L
                        cnt += 1
                        Q.append((xx, yy))
            res.append(cnt)
            L+=1
print(len(res))
res.sort()
for x in res:
    print(x)
