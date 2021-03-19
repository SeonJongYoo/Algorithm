# 피자 배달 거리(DFS)


# 내가 작성한 코드
# 6개의 피자집 중에 4개의 피자집을 선택 - 조합 문제!!!!
# 문제 이해를 잘못했다. 문제에 상하좌우를 회전하여 탐색하라는 말은 없다!!
dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
def DFS(x, y, L):
    global cnt, flag
    Min = 2147000000
    if L == 6:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
        print("------------------")
    else:
        # 집을 중심으로 "시계방향"에 피자집이 있는지 확인
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and board[xx][yy] != 0 and dis[xx][yy] == 0:
                if board[x][y] == 1 and board[xx][yy] == 2:  # 현재 피자집을 남기는 경우
                    if abs(x-xx) + abs(y-yy) < Min:
                        Min = abs(x - xx) + abs(y - yy)
                        dis[x][y] = Min
                DFS(xx, yy, L+1)

                if board[xx][yy] == 2:  # 현재 피자집을 폐업하는 경우
                    board[xx][yy] = 0
                DFS(xx, yy, L+1)
                if board[xx][yy] == 0:
                    board[xx][yy] = 2


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dis = [[0]*n for _ in range(n)]
    cnt = 0
    flag = False
    DFS(0, 0, 0)


# 내가 작성한 코드2 - 정답
# 문제에서 좌표에 대해 상하좌우를 탐색하라는 말은 없다!!!!!
# house리스트와 pizza리스트를 선언하여 각각 해당 좌표를 저장한다.
# pizza리스트에서 m개를 선택하는 조합 알고리즘을 수행한다!!
# 조합 문제 응용!!
def DFS(L):
    global Min
    if L == len(pz):
        cnt = 0
        for i in range(len(pz)):
            if ch[i] == 1:
                cnt += 1
        if cnt == m:
            dis = [[0]*n for _ in range(n)]  # 새로운 조합이 나올 때마다 dis리스트는 새로 초기화해야한다.
            for i in range(len(pz)):
                if ch[i] == 1:
                    for x in hs:
                        if dis[x[0]][x[1]] == 0:
                            dis[x[0]][x[1]] = abs(pz[i][0] - x[0]) + abs(pz[i][1] - x[1])
                        elif abs(pz[i][0] - x[0]) + abs(pz[i][1] - x[1]) <= dis[x[0]][x[1]]:
                            dis[x[0]][x[1]] = abs(pz[i][0] - x[0]) + abs(pz[i][1] - x[1])
            Sum = 0
            for i in range(n):
                for j in range(n):
                    if dis[i][j] != 0:
                        Sum += dis[i][j]
            if Sum < Min:
                Min = Sum
    else:
        ch[L] = 1
        DFS(L+1)
        ch[L] = 0
        DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    Min = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            if board[i][j] == 2:
                pz.append((i, j))
    ch = [0] * len(pz)
    DFS(0)
    print(Min)


# 강의 코드
def DFS(L, s):
    global res
    if L == m:
        Sum = 0
        for j in range(len(hs)):  # 집
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:  # 피자집
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            Sum += dis
        if Sum < res:
            res = Sum
    else:
        for i in range(s, len(pz)):  # 조합 구하기에선 s의 역할이 가장 중요!!!
            cb[L] = i  # 선택된 피자집 체크
            DFS(L+1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dis = [[0]*n for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m  # 조합 구하기
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            if board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)