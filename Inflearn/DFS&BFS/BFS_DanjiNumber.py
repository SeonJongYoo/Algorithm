# 단지 번호 붙이기(BFS)

# 내가 작성한 코드
# 주어진 격자판을 모두 탐색할 생각을 못했다!!!!!!
from collections import deque
n = int(input())
board = [list(input()) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
tQ = deque()
L = 1
if board[0][0] == '1':
    ch[0][0] = L
Q.append((0, 0))
while True:
    size = len(Q)
    if size == 0:
        L += 1
        if not tQ:
            break
        tmp1 = tQ.popleft()
        Q.append(tmp1)
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= n-1 and 0 <= y <= n-1:
            if board[x][y] == '1' and ch[x][y] == 0:
                ch[x][y] = L
                Q.append((x, y))
            elif board[x][y] == '0' and ch[x][y] == 0:
                board[x][y] = '3'
                tQ.append((x, y))
# 1 0 1    1 0 2
# 0 1 0 => 0 2 0
# 0 0 1    0 0 4
# 위와 같은 경우 대각선임에도 같은 단지로 처리하는 에러 발생
res = set()
for i in range(n):
    for j in range(n):
        if ch[i][j] != 0:
            res.add(ch[i][j])
print(len(res))
temp = []
while res:
    cnt = 0
    x = res.pop()
    for i in range(n):
        for j in range(n):
            if ch[i][j] == x:
                cnt += 1
    temp.append(cnt)
temp.sort()
for x in temp:
    print(x)


# 강의 코드
# 집을 만나면 0으로 바꾼다.
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
cnt = 0
res = []
Q = deque()
# ******************************************
# 이중 for문이 돌면서 board의 좌표값이 1인 부분을 Q에 넣고 탐색을 시작한다.
for i in range(n):
    for j in range(n):
# ******************************************
        if board[i][j] == 1:  # 집을 만나는 경우 1 -> 0으로 변경
            board[i][j] = 0
            Q.append((i, j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 0:
                        continue
                    board[x][y] = 0
                    Q.append((x, y))
                    cnt += 1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)