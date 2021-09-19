# 나이트의 이동

import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
for _ in range(t):
    length = int(sys.stdin.readline().rstrip())
    cx, cy = map(int, sys.stdin.readline().rstrip().split())
    tx, ty = map(int, sys.stdin.readline().rstrip().split())
    board = [[0]*length for _ in range(length)]
    Q = deque()
    Q.append((cx, cy))
    board[cx][cy] = 1
    while Q:
        tmp = Q.popleft()
        if board[tx][ty] != 0:
            print(board[tx][ty] - 1)
            break
        for i in range(8):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0 <= xx < length and 0 <= yy < length and board[xx][yy] == 0:
                board[xx][yy] = board[tmp[0]][tmp[1]] + 1
                Q.append((xx, yy))

        # for i in range(length):
        #     for j in range(length):
        #         print(board[i][j], end=" ")
        #     print()
        # print("-----------------------")