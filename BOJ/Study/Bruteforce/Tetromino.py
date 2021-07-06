# 테트로미노


import sys


def DFS(L, x, y, Sum):
    global Max
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return
    if L == 4:
        if Sum < Max:
            return
        # print("x, y: ", x, y)
        # for i in range(n):
        #     for j in range(m):
        #         print(visit[i][j], end=" ")
        #     print()
        # print("Sum: ", Sum)
        Max = max(Sum, Max)
        # print("Max: ", Max)
        # print("-----------------------------")
    else:
        if visit[x][y] == 0:
            visit[x][y] = 1
            DFS(L + 1, x - 1, y, Sum + board[x][y])
            DFS(L + 1, x, y + 1, Sum + board[x][y])
            DFS(L + 1, x + 1, y, Sum + board[x][y])
            DFS(L + 1, x, y - 1, Sum + board[x][y])
            visit[x][y] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
Max = 0
for i in range(n):
    for j in range(m):
        DFS(0, i, j, 0)
        #print("i, j: ", i, j)
        t1, t2 = 0, 0
        for k in range(4):
            if k == 3:
                tmp1, tmp2 = 0, 0
                if 0 <= i + 1 < n and 0 <= j + 1 < m:
                    tmp1 = board[i + 1][j + 1]
                if 0 <= i - 1 < n and 0 <= j + 1 < m:
                    tmp2 = board[i - 1][j + 1]
                t1 += max(tmp1, tmp2)
            else:
                if 0 <= j + k < m:
                    t1 += board[i][j + k]
                else:
                    t1 = 0
                    break
        for k in range(4):
            if k == 3:
                tmp1, tmp2 = 0, 0
                if 0 <= i + 1 < n and 0 <= j + 1 < m:
                    tmp1 = board[i + 1][j + 1]
                if 0 <= i + 1 < n and 0 <= j - 1 < m:
                    tmp2 = board[i + 1][j - 1]
                t2 += max(tmp1, tmp2)
            else:
                if 0 <= i + k < n:
                    t2 += board[i+k][j]
                else:
                    t2 = 0
                    break
        #print(t1, t2)
        Max = max(Max, t1, t2)
        #print("Max: ", Max)
        #print("----------------")
print(Max)