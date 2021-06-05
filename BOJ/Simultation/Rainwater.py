# 빗물


def DFS(x, y):
    global res, tmp
    if y == w:
        tmp = 0
        return
    if board[x][y] == 1:
        res += tmp
        tmp = 0
    else:
        tmp += 1
        board[x][y] = 2
        DFS(x, y+1)


h, w = map(int, input().split())
arr = list(map(int, input().split()))
board = [[0]*w for _ in range(h)]
k = 0
tmp = 0
res = 0
for i in range(w):
    for j in range(h-1, h-arr[k]-1, -1):
        board[j][i] = 1
    k += 1
for i in range(h-1, -1, -1):
    for j in range(w):
        if board[i][j] == 1:
            DFS(i, j+1)
print(res)