# 등산경로(DFS)


# 내가 작성한 코드 - 정답
# 문제 조건 주의하기!! - 출발점은 가장 낮은 곳!, 도착점은 가장 높은 곳!
def DFS(L, x, y):
    global cnt
    if dis[mx][my] == 1:
        cnt += 1
    else:
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 <= n-1 and 0 <= y1 <= n-1 and board[x1][y1] > board[x][y]:
                if dis[x1][y1] == 0:
                    dis[x1][y1] = 1
                    DFS(L+1, x1, y1)
                    dis[x1][y1] = 0  # 이전 상황으로 돌아오므로 체크를 풀어준다.


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    Max = -214700000
    Min = 2417000000
    mx, my = 0, 0
    mx1, my1 = 0, 0
    # 가장 낮은 지점과 가장 높은 지점 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] > Max:
                Max = board[i][j]
                mx, my = i, j  # 최댓값의 좌표
            if board[i][j] < Min:
                Min = board[i][j]
                mx1, my1 = i, j  # 최솟값의 좌표
    dis = [[0]*n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dis[mx1][my1] = 1
    cnt = 0
    DFS(0, mx1, my1)
    print(cnt)


# 강의 코드 - 내 코드와 완전 일치
