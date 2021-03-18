# 섬나라 아일랜드(BFS)


# 내가 작성한 코드
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0, 1, -1, 1, -1] # 대각선도 탐색한다.
dy = [0, 1, 0, -1, 1, 1, -1, -1]
Q = deque()
cnt = 0
L = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            L += 1
            board[i][j] = 0
            ch[i][j] = L
            Q.append((i, j))
        while Q:
            tmp = Q.popleft()
            for k in range(8):
                x = tmp[0] + dx[k]
                y = tmp[1] + dy[k]
                if 0 <= x <= n-1 and 0 <= y <= n-1 and board[x][y] == 1:
                    Q.append((x, y))
                    board[x][y] = 0
                    ch[x][y] = L
res = set()
for i in range(n):
    for j in range(n):
        if ch[i][j] != 0:
            res.add(ch[i][j])
print(len(res))


# 강의 코드
# 단지 번호 붙이기와 같은 문제
from collections import deque
dx = [-1, 0, 1, 0, 1, -1, 1, -1] # 대각선도 탐색한다.
dy = [0, 1, 0, -1, 1, 1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            while Q:  # Q가 끝나면 한번의 BFS가 종료된 것
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt += 1
print(cnt)