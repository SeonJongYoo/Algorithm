# 사다리 타기(DFS)


# 내가 작성한 코드 - 정답
dx = [0, 0, 1]
dy = [-1, 1, 0]
def DFS(x, y):
    global scol, flag
    if flag:
        return
    if board[x][y] == 1:
        ch[x][y] = 1
        for i in range(3):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < 10 and 0 <= yy < 10 and board[xx][yy] != 0 and ch[xx][yy] == 0:
                if i == 0 or i == 1:  # 왼쪽 or 오른쪽에 있는 좌표인 경우
                    if board[xx][yy] == 2:
                        ch[xx][yy] = 2
                        flag = True
                    else:
                        ch[xx][yy] = 1
                        DFS(xx, yy)
                    break  # 아래쪽을 탐색할 필요없으므로 바로 break!
                else:
                    if board[xx][yy] == 2:
                        ch[xx][yy] = 2
                        flag = True
                    else:
                        ch[xx][yy] = 1
                        DFS(xx, yy)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    scol = 0
    flag = False
    for i in range(10):
        if flag:
            break
        scol = i
        ch = [[0] * 10 for _ in range(10)]
        DFS(0, i)
    print(scol)


# 강의 코드
# 9행을 먼저 탐색하여 2를 찾는다.
# 2부터 시작하여 1을 만나면 왼쪽 or 오른쪽을 먼저 탐색하고 위쪽을 탐색한다. - 내 코드와 일치
def DFS(x, y):
    ch[x][y] = 1  # 방문한 좌표는 1로 체크
    if x == 0:
        print(y)  # 0행에 도착하면 현재의 열번호를 출력
    else:
        if y-1 > 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:  # 현재 좌표에서 왼쪽 탐색
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0: # 현재 좌표에서 오른쪽 탐색
            DFS(x, y+1)
        else:  # 현재 좌표에서 위쪽을 탐색
            DFS(x-1, y)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)