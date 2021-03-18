# 미로탐색(DFS)


# 내가 작성한 코드 - 정답
def DFS(x, y):
    global cnt
    if board[6][6] != 0:
        cnt += 1
        board[x][y] = 0
    else:
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 <= 6 and 0 <= y1 <= 6 and board[x1][y1] == 0:
                board[x1][y1] = 3
                DFS(x1, y1)
                board[x1][y1] = 0  # 이전 상황으로 돌아오므로 체크를 풀어야한다.


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    board[0][0] = 3
    DFS(0, 0)
    print(cnt)


# 강의 코드 - 내 코드와 완전 일치
# 최단 거리 문제X
# 단순히 모든 경로를 찾으면 된다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= y <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)