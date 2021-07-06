# 사탕 게임

import sys


# 연속된 값을 찾아야한다!!
def checkRow():
    global Max
    tmp = 0
    while tmp < n:
        cnt = 1
        tmp1 = arr[tmp][0]
        for i in range(1, n):
            if tmp1 == arr[tmp][i]:
                cnt += 1
                Max = max(cnt, Max)
            else:
                cnt = 1
            tmp1 = arr[tmp][i]
        if Max == n:
            return
        tmp += 1


def checkCol():
    global Max
    tmp = 0
    while tmp < n:
        cnt = 1
        tmp1 = arr[0][tmp]
        for i in range(1, n):
            if tmp1 == arr[i][tmp]:
                cnt += 1
                Max = max(cnt, Max)
            else:
                cnt = 1
            tmp1 = arr[i][tmp]
        if Max == n:
            return
        tmp += 1


n = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
Max = 1
# 교환 전 최댓값을 먼저 구한다.
checkRow()
checkCol()
if Max != n:
    for i in range(n):
        for j in range(n):
            if Max == n:
                print(n)
                sys.exit(0)
            for k in range(2):
                xx = i + dx[k]
                yy = j + dy[k]
                if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] != arr[i][j]:
                    arr[i][j], arr[xx][yy] = arr[xx][yy], arr[i][j]
                    checkRow()
                    checkCol()
                    arr[i][j], arr[xx][yy] = arr[xx][yy], arr[i][j]
print(Max)