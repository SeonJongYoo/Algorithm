# 단지 번호 붙이기(DFS)

# DFS
# board[i][j] == 1인 곳을 방문하면 0으로 바꿔버린다.
# 다음번 탐색 때 이미 방문한 곳을 그냥 지나치게 할 수 있음
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4): # 상하좌우 탐색
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= y < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 새로운 단지를 만났을 때
                cnt = 0  # 집의 개수 세기
                DFS(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()
    for x in res:
        print(x)