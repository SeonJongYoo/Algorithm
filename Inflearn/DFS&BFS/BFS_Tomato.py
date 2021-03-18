# 토마토(BFS)


# 내가 작성한 코드
# 토마토가 익는 날짜는 어떻게 계산하지?
from collections import deque
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*m for _ in range(n)]  # 날짜 기록
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
res = set()
for i in range(n):
    for j in range(m):
        res.add(board[i][j])
if 0 not in res:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                Q.append((i, j))
                # 익은 토마토(값이 1)들의 위치를 먼저 큐에 넣어준다.
                # 이 생각도 중요!
    while Q:
        tmp = Q.popleft()
        for k in range(4):
            x = tmp[0] + dx[k]
            y = tmp[1] + dy[k]
            if 0 <= x <= n-1 and 0 <= y <= m-1 and board[x][y] == 0:
                Q.append((x, y))
                board[x][y] = 1  # 안익은 토마토를 익은 토마토로 변경
                ch[x][y] = ch[tmp[0]][tmp[1]] + 1  # 날짜 계산

ck = False
result = 0
for i in range(n):
    if ck:
        break
    for j in range(m):
        if board[i][j] == 0:  # 0이 하나라도 있다면 -1출력하고 break!
            print(-1)
            ck = True
            break
        if ch[i][j] > result:
            result = ch[i][j]
if not ck:
    print(result)



# 강의 코드
# 익은 토마토들을 먼저 탐색하면서 큐에 push
# 익은 토마토들을 큐에서 pop하면서 안익은 토마토들을 1로 변경하고 큐에 추가
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# ******************************
dis = [[0]*n for _ in range(m)]  # 날짜 기록 리스트 - 익은 토마토의 위치에서 시계방향으로 돌면서
# 익지 않은 토마토들을 찾고 그것을 dis리스트의 현재 값에 +1로 만들어준다.
# ******************************
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1  # 안익은 토마토를 익은 토마토로 변경
            # *************핵심!!******************
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1  # 날짜 계산
            # *******************************
            Q.append((xx, yy))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
        print(result)
else:
    print(-1)