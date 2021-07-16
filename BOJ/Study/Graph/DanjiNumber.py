# 단지번호붙이기

import sys


def DFS(x, y, home):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    else:
        if city[x][y] == 1 and visit[x][y] == 0:
            visit[x][y] = home
            cnt += 1
            DFS(x-1, y, home)
            DFS(x, y+1, home)
            DFS(x+1, y, home)
            DFS(x, y-1, home)


n = int(sys.stdin.readline().rstrip())
city = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
k = 1
res = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1 and visit[i][j] == 0:
            cnt = 0
            DFS(i, j, k)
            res.append(cnt)
            k += 1
print(len(res))
res.sort()
for a in res:
    print(a)