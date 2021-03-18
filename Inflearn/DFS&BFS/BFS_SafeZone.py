# 안전영역(BFS)


# 내가 작성한 코드
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Max = -2147000000
tMin = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > Max:
            Max = board[i][j]
Q = deque()
res = 0
while tMin < Max:
    L = 0
    tboard = []  # 기존의 board는 건드리면 안되므로 tboard로 board와 똑같은 격자판 선언
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        t = []
        for j in range(n):
            t.append(board[i][j])
        tboard.append(t)
    for i in range(n):
        for j in range(n):
            if tboard[i][j] > tMin:
                L += 1
                tboard[i][j] = 0
                Q.append((i, j))
                ch[i][j] = L
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x <= n-1 and 0 <= y <= n-1 and tboard[x][y] > tMin:
                        tboard[x][y] = 0
                        Q.append((x, y))
                        ch[x][y] = L
    for i in range(n):
        for j in range(n):
            if ch[i][j] != 0 and ch[i][j] > res:
                res = ch[i][j]
    tMin += 1
print(res)


# 강의 코드 - DFS
import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10**6)
def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__=="__main__":
    n = int(input())
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:  # 안전영역 발견
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:  # 안전영역이 없으면 break
            break
    print(res)